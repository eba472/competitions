#### TCP : transmission control protocol
- High level protocols that uses TCP examples
  - HTTP: Hypertext transfer protocol
  - SSH: Secure Shell
  - IMAP: internet access protocol


#### IP : Internet protocol
- Every device has IP address


##### TCP/IP : default method of data communication on internet
- Breaks messages into packets to avoid resending whole when problem occurs
- Assembled automatically
- Every packet can take different route
- Maintains connection until exchange is over
- 4 layers
  - Datalink layer: handles the physical act of sending and receiving data.
  - Internet layer: Send packets from a network and controlling their movement across a network to ensure they reach their destination. 
  - Transport layer: provide a solid and reliable data connection between the original application or device and its intended destination. This is the level where data is divided into packets and numbered to create a sequence. The transport layer then determines how much data must be sent, where it should be sent to, and at what rate. It ensures that data packets are sent without errors and in sequence and obtains the acknowledgment that the destination device has received the data packets.
  - Application layer: The application layer refers to programs that need TCP/IP to help them communicate with each other. This is the level that users typically interact with, such as email systems and messaging platforms. It combines the session, presentation, and application layers of the OSI model.