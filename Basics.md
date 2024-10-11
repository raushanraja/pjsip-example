### PJSUA2
- High level API for contructing SIP Applicatoin.
- It wraps:
    - Signaming
    - Media
    - NAT (STUN, TURN, ICE)
    - Account Management
    - Buddy list Management
    - Presence
    - IM
    - Local Conferenceing
    - File Streaming
    - Local Playback
    - Voice Recording

#### Main Classes:
- Endpoint
    - This is the main class
    - Need to be instaintiated only once
    - This instance can then initialize and start the library.

- Account
    - Specifies the identity of the Endpoint
    - At least one account needs to be created before anything

- Media
    - Abstrace base class representing the media element
    - Capable of either creating or consuming the media
    - Further subclassed into other classes such as AudioMedia

- Call
    - It represents ongoing call (technically INVITE)
    - Use to manipulate call (Accept, Decline, Hole, Transfer etc.).

- Buddy
    - Represents a remote Endpoint
    - Allows subscribing to presence status of remote endpoing for Buddy's status (online, offline. etc.)
    - Allows sending and receiving instant messages to/from the buddy.


#### General Concepts:
- Class Usages Patterns:
    - Each of the main class (Endpoint, Call, Account, or Buddy) get their events/notification in callback methods.
    - To handle these events, derive from correspondig class and implement/override relevant method

- Asynchronous Operations:
    - All operation involving sending/receiving SIP messages are asynchronous.
    - Functions that invoke these operation will complete immediately but it does not mean they have successfully done the work.
    - The completion status are given to the callbacks. So wait for the callbacks for any status
    

- Threading:
    - PJSUA2 with high level languages such as Python, it is required to disable PJSUA2 internal worker threads by setting EpConfig.uaConfig.threadCnt to 0.
Because the high level environment doesn’t like to be called by external thread (such as PJSIP’s worker thread).
