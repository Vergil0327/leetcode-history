## Background

**BBR** is a TCP congestion control algorithm developed by Google. It aims to make Internet data transfers faster, which is no small feat!

*ps. BBR is short for Bottleneck Bandwidth and Round-trip propagation time*
further reading of BBR
- [Google TCP BBR Congestion Control](https://blog.maxkit.com.tw/2019/01/google-tcp-bbr-congestion-control.html)
- [TCP BBR擁塞控制算法解析](https://blog.csdn.net/ebay/article/details/76252481)
- [Linux Kernel 4.9 中的 BBR 算法與之前的 TCP 擁塞控制相比有什麼優勢？](https://www.zhihu.com/question/53559433)

### How Spotify Streams Music

- store each encoded music track as a file
- copied on HTTP servers across the world

When a user plays a song, the Spotify app will fetch the file in chunks from a nearby server with HTTP GET range requests. A typical chunk size is 512kB.

Tracking metrics:

1. Playback latency, the time from click to sound.
2. Stutter, the number of skips/pauses during playback.
   - Stutter happens mostly due to audio buffer underruns when download bandwidth is low

metrics map closely to connection time and transfer bandwidth

Now, how could BBR improve our streaming?

## TCP Congestion What?

see:
`server --> file transfer --> client`

- server sends data in TCP packets
- client confirms delivery by returning ACKs
- connection has a limited capacity depending on hardware and network conditions

If the server sends too many packets too quickly, they will simply be dropped along the way. The server registers this as missing ACKs

The role of a congestion control algorithm is to look at the flow of send+ACKs and decide on a send rate. ex. **CUBIC** algorithm

 **CUBIC** focus on packet loss.
 
 As long as there is no packet loss, they increase send rate, and when packets start disappearing, they back off.

**Problem of CUBIC**

 One problem with this approach is a tendency to overreact to small amounts of random packet loss, interpreting it as a sign of congestion.

**Solution to Solve - BBR**

**BBR** looks at round trip time and arrival rate of packets to build an internal model of the connection capacity

Once it has measured the current bandwidth, it keeps the send rate at that level even if there is some noise in the form of packet loss.

[more BBR](https://www.ietf.org/proceedings/97/slides/slides-97-iccrg-bbr-congestion-control-02.pdf)

## The Experiment

Many internet protocol changes require coordinated updates to clients and servers (ex. IPv6!).

**BBR is different!**

it only needs to be enabled on the sender’s side. It can even be enabled after the socket is already opened

**A/B Test**

Spotify set up a random subset of users to include “bbr” in the audio request hostname as a flag (feature flag). The other requests get served using the default, CUBIC.

## Results

- Taking daily averages, stutter **decreased** **6-10%** for the **BBR** group
- Bandwidth **increased** by **10-15%** for the slower download cohorts, and by **5-7%** for the median.
- There was no difference in latency between groups.

**Significant Variation Across Geo Regions**

most of the improvements in Asia-Pacific and Latin America, with **17%** and **12%** **decreases** in stutter, respectively

Bandwidth **increased** **15-25%** for slower downloads, and around **10%** for the median.

*By comparison, Europe and North America had **3-5%** improvement in stutter, and around **5%** in bandwidth.*