[2017 - Netflix: What Happens When You Press Play?](http://highscalability.com/blog/2017/12/11/netflix-what-happens-when-you-press-play.html)

**Netflix operates in two clouds**

1. AWS
2. Open Connect

Both clouds must work together seamlessly to deliver endless hours of customer-pleasing video.

**The three parts of Netflix**
1. client
   - user interface on any device used to browse and play Netflix videos. ex. app or website
2. backend
   - Everything that happens **before** you hit play happens in the backend, which runs in `AWS`
     - preparing all new incoming video
     -  handling requests from all apps, websites, TVs, and other devices
   - Everything that happens **after** you hit play is handled by `Open Connect`
     - Netflix’s custom global content delivery network (CDN)
     - Open Connect stores Netflix video in different locations throughout the world
3. content delivery network (CDN)

By controlling all three areas—`client`, `backend`, `CDN`— Netflix has achieved complete vertical integration. 


**What Happens In AWS Before You Press Play?**

- Scalable computing and scalable storage

Scalable computing is **EC2** and scalable storage is **S3**

- Scalable distributed database

Netflix uses both **DynamoDB** and **Cassandra** for their distributed databases

  - *Database*
    -  A database stores data
  - *Distributed*
    - Distributed means the database doesn’t run on one big computer, it runs on many computers
  - Scalable
    - Scalable means the database can handle as much data as you ever want to put into it

- Big data processing and analytics

Big data simply means there’s a lot of data. Netflix collects a lot of information.

Putting all the data in a standard format is called *processing*.
Making sense of all that data is called *analytics*.
Data is analyzed to answer specific questions.

**Recommendations**

Usually Netflix will show you only 40 to 50 video options, yet they have many thousands of videos available. 

How does Netflix decide? Using *machine learning*.

### Transcoding From Source Media To What You Watch

Here’s where we start transitioning into how video is handled by Netflix.

**Transcoding or Encoding**
  - Netflix convert the video into a format that works best for your device
  - Transcoding is the process that converts a video file from one format to another, to make videos viewable across different platforms and devices.

**The source of source media**

Who sends video to Netflix? Production houses and studios. Netflix calls this *video source media*. The new video is given to the *Content Operations Team* for processing.

Before you can view a video, Netflix puts it through a rigorous multi-step process.

1. Validating the video

The video is rejected if any problems are found.

2. Into the media pipeline

A pipeline is simply a series of steps data is put through to make it ready for use, much like an assembly line in a factory.

It’s not practical to process a single multi-terabyte sized file, so the first step of the pipeline is to break the video into lots of smaller chunks. 

The video chunks are then put through the pipeline so they can be encoded *in parallel*.

3. The result is a pile of files

The encoding process creates a lot of files. Why? The end goal for Netflix is to support every internet-connected device.

- Netflix creates files optimized for different network speeds
- Audio is encoded into different levels of quality and in different languages
- A video may have subtitles in a number of different languages

Just how many files are we talking about?

For The Crown, Netflix stores around 1,200 files. Stranger Things season 2 has even more files.

### Three Different Strategies For Streaming Video

Netflix has tried three different video streaming strategies:
- its own small CDN
- third-party CDNs
- Open Connect.

For Netflix, the central location where videos are stored is S3. 
**Why Build A CDN?**

The biggest benefits of a CDN are speed and reliability. 

The idea behind a CDN is simple: put video as close as possible to users by spreading computers throughout the world

- The First CDN Was Too Small
- The Second CDNs Were Too Big
- Open Connect Was Just Right

In 2011, Netflix realized at its scale it needed a dedicated CDN solution to maximize network efficiency. Video distribution is a core competency for Netflix and could be a huge competitive advantage.

So Netflix started developing Open Connect, its own purpose-built CDN.

advantages:

1. Less expensive: 3rd-party CDNs are expensive. Doing it themselves would save a lot of money
2. Better quality: By controlling the entire video path—transcoding, CDN, clients on devices—Netflix reasoned it could deliver a superior video viewing experience
3. More Scalable: Quickly supporting all those people while providing a quality video viewing experience required building its own system

### Finally: Here’s What Happens When You Press Play

- Netflix can be divided into three parts: the backend, the client, and the CDN. 
- All requests from Netflix clients are handled in AWS.
- All video is streamed from a nearby Open Connect Appliance (OCA) in the Open Connect CDN.
- Netflix operates out of three AWS regions and can usually handle a failure in any region without members even noticing.
- New video content is transformed by Netflix into many different formats so the best format can be selected for viewing based on the device type, network quality, geographic location, and the member’s subscription plan.
- Every day, over Open Connect, Netflix distributes video throughout the world, based on what they predict members in each location will want to watch.

1. You select a video to watch using a client running on some device. The client sends a play request, indicating which video you want to play, to Netflix’s Playback Apps service running in AWS.
2. We’ve not talked about this before, but a big part of what happens after you hit play has to do with licensing. Not every location in the world has a license to view every video. Netflix must determine if you have a valid license to view a particular video. We won’t talk about how that works—it’s really boring—but keep in mind it’s always happening. One reason Netflix started developing its own content is to avoid licensing issues. Netflix wants to release a show to everyone in the world all at the same time. Creating its own content is the easiest way for Netflix to avoid worrying about licensing problems.
3. Taking into account all the relevant information, the Playback Apps service returns URLs for up to ten different OCA servers. These are the same sort of URLs you use all the time in your web browser. Netflix uses your IP address and information from ISPs to identify which OCA clusters are best for you to use.
4. The client intelligently selects which OCA to use. It does this by testing the quality of the network connection to each OCA. It will connect to the fastest, most reliable OCA first. The client keeps running these tests throughout the video streaming process.
5. The client probes to figure out the best way to receive content from the OCA.
6. The client connects to the OCA and starts streaming video to your device. 
7. Have you noticed when watching a video the picture quality varies? Sometimes it will look pixelated, and after awhile the picture snaps back to HD quality? That’s because the client is adapting to the quality of the network. If the network quality declines, the client lowers video quality to match. The client will switch to another OCA when the quality declines too much.