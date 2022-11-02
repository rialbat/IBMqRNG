import qiskit
from qiskit import IBMQ, transpile
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
            return 1
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

def getCloudServers():
    global provider
    return provider.backends()

def updateProvider(status):
    global provider
    if status == 0:
        provider = IBMQ.get_provider('ibm-q')
    else:
        provider = qiskit.BasicAer

def getLocalServers():
    return qiskit.Aer.backends()

def createCircuit(n):
    qr = qiskit.QuantumRegister(n)
    cr = qiskit.ClassicalRegister(n)
    circuit = qiskit.QuantumCircuit(qr, cr)
    circuit.h(qr)
    circuit.measure(qr, cr)
    return circuit

def createRequest(qbits, backend, shots):
    simulator = provider.get_backend(backend)

    circ = transpile(createCircuit(qbits), simulator)

    result = simulator.run(circ, shots=shots, memory=True).result()
    return result

def getServerStatus(backsys):
    global provider
    backend = provider.get_backend(backsys)
    return backend.status().status_msg

def getServerStatus(backsys):
    global provider
    backend = provider.get_backend(backsys)
    return backend.status().status_msg

def getPendingJobs(backsys):
    global provider
    backend = provider.get_backend(backsys)
    return backend.status().pending_jobs



