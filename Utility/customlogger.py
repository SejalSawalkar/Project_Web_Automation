import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log")
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        return log


#execute
# pytest -v -s --log-file=Logs/log.log