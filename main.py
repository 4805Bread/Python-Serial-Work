import serial.tools.list_ports
import serial
if __name__ == '__main__':
    i = 0
    #Scan and print available ports
    print("Port Search...")
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports:
        print(port.description)
    portNames = [port.name for port in ports]

    #Prompt user for port to attach to
    invalidEntry = True
    while invalidEntry:
        selectedPort = input("Enter COM port (syntax: COMx or x)\n")
        if selectedPort.isdigit():
            selectedPort = "COM"+selectedPort

        if selectedPort in portNames:
            invalidEntry = False
        else:
            print("Port " + selectedPort + " not available.\nAvailable ports:")
            for port in ports:
                print(port.description)

    #Open port and print 5 responses
    with serial.Serial(selectedPort, 9600, timeout=1) as ser:
        while i < 5:
            print(ser.readline())
            i += 1

