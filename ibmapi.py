import qiskit
from qiskit import IBMQ
import datetime


def IBMQLogin(token):
    global provider
    if token == "":
        return -1
    else:
        try:
            IBMQ.save_account(token, overwrite=True)
            IBMQ.load_account()
            provider = IBMQ.get_provider('ibm-q')
        except Exception as ex:
            with open("ErrorLog.txt", "a") as f:
                f.write('\n' + str(datetime.datetime.now()) + '\n' + str(ex.args))
            if str(ex.args).find("Forbidden for url") > 0:
                print("Forbidden for url. Error: -2")
                return -2
            elif str(ex.args).find("Max retries exceeded") > 0:
                print("Max retries exceeded. Error: -3")
                return -3
            elif str(ex.args).find("Login failed") > 0:
                print("Login failed. Error: -4")
                return -4
            else:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                return -5
        finally:
            return 1



