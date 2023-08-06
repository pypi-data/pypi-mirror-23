import shlex
import logging
import subprocess
import os
import signal
import psutil
import time

logger = logging.getLogger("rally.process")


def run_subprocess(command_line):
    logger.debug("Running subprocess [%s]" % command_line)
    return os.system(command_line)


def run_subprocess_with_output(command_line):
    logger.debug("Running subprocess [%s] with output." % command_line)
    command_line_args = shlex.split(command_line)
    command_line_process = subprocess.Popen(
        command_line_args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    has_output = True
    lines = []
    while has_output:
        line = command_line_process.stdout.readline()
        if line:
            lines.append(line.decode("UTF-8").strip())
        else:
            has_output = False
    command_line_process.wait(timeout=5)
    return lines


def run_subprocess_with_logging(command_line, header=None, level=logging.INFO):
    logger.debug("Running subprocess [%s] with logging." % command_line)
    """
    Runs the provided command line in a subprocess. All output will be captured by a logger.

    :param command_line: The command line of the subprocess to launch.
    :param header: An optional header line that should be logged (on info level)
    :return: True iff the subprocess has terminated successfully.
    """
    command_line_args = shlex.split(command_line)
    if header is not None:
        logger.info(header)
    logger.debug("Invoking subprocess '%s'" % command_line)
    try:
        command_line_process = subprocess.Popen(
            command_line_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        has_output = True
        while has_output:
            line = command_line_process.stdout.readline()
            if line:
                logger.log(level=level, msg=line)
            else:
                has_output = False
        command_line_process.wait(timeout=5)
        logger.debug("Subprocess [%s] finished with return code [%s]." % (command_line, str(command_line_process.returncode)))
        return command_line_process.returncode == 0 or command_line_process.returncode is None
    except OSError:
        logger.exception("Exception occurred when running [%s]." % command_line)
        return False


def kill_running_es_instances(trait):
    """
    Kills all instances of Elasticsearch that are currently running on the local machine by sending SIGKILL.

    :param trait some trait of the process in the command line.
    """
    def elasticsearch_process(p):
        return p.name() == "java" and any("elasticsearch" in e for e in p.cmdline()) and any(trait in e for e in p.cmdline())

    logger.info("Killing all processes which match [java], [elasticsearch] and [%s]" % trait)
    kill_all(elasticsearch_process)


def kill_running_rally_instances():
    def rally_process(p):
        return p.name() == "esrally" or \
               p.name() == "rally" or \
               (p.name().lower().startswith("python")
                and any("esrally" in e for e in p.cmdline())
                and not any("esrallyd" in e for e in p.cmdline()))

    kill_all(rally_process)


def kill_all(predicate):
    # no harakiri please
    my_pid = os.getpid()
    for p in psutil.process_iter():
        try:
            if p.pid == my_pid:
                logger.info("Skipping myself (PID [%s])." % p.pid)
            elif predicate(p):
                logger.info("Killing lingering process with PID [%s] and command line [%s]." % (p.pid, p.cmdline()))
                p.kill()
                # wait until process has terminated, at most 3 seconds. Otherwise we might run into race conditions with actor system
                # sockets that are still open.
                for i in range(3):
                    try:
                        p.status()
                        time.sleep(1)
                    except psutil.NoSuchProcess:
                        break
            else:
                logger.debug("Skipping [%s]" % p.cmdline())
        except (psutil.ZombieProcess, psutil.AccessDenied) as e:
            logger.debug("Skipping process: [%s]" % str(e))
