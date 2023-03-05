---
categories:
- 读书笔记
date: 2022-12-17 15:59:07
password: null
sticky: 100
tags:
- tcp
- ipv6
- internet
- ipv4
- introduction
title: tcpip详解读书笔记
---

> 

<!--more-->

# Chapter 1 Introduction

## 1.1 Architectural Principles

### 1.1.1 Packets, Connections, and Datagrams

分组交换->多路复用

FIFO->统计复用

数据报: 所有识别信息都位于分组中而不是交换机中

消息边界: 大部分数据报协议是保留消息边界的(UDP), 但是在电路交换和虚电路网络中, 不会保留消息边界(TCP)

### 1.1.2 The End-to-End Argument and Fate Sharing

端到端论点: 只有在通信系统端角度的应用知识的帮助下，才能完全和正确地实现问题中提到的功能。因此，作为通信自身的一个特点，不可能提供有疑问的功能。（有时， 通信系统提供的一个功能不完整的版本可能用于提高性能。）

命运共享: 建议所有必要的状态放在通信端点

### 1.1.3 Error Control and Flow Control

差错控制: 网络中, 尽力而为

流量控制: 端

## 1.2 Design and Implementation

### 1.2.1 Layering

从底层到高层数字递增

5 层 TCP/IP

7 层 OSI

### 1.2.2 Multiplexing, Demultiplexing, and Encapsulation in Layered Implementations

PDU 协议数据单元

switch, bridge 对网络层透明

## 1.3 The Architecture and Protocols of the TCP/IP Suite

### 1.3.1 The ARPANET Reference Model

三种类型 ip 地址: 

单播, 广播, 组播

ICMP, IGMP

DCCP, SCTP

### 1.3.2 Multiplexing, Demultiplexing, and Encapsulation in TCP/IP

每层都有一个标识符

### 1.3.3 Port Numbers

熟知端口号: 0~1023

注册端口号: 1024~49151, 它们松散地绑定于一些服务。也就是说有许多服务绑定于这些端口，这些端口同样用于许多其它目的。例如：许多系统处理动态端口从1024左右开始。

私有端口号: 49152~65535, 理论上，不应为服务分配这些端口。实际上，机器通常从1024起分配动态端口。但也有例外：SUN的RPC端口从32768开始。

奇数端口号

### 1.3.4 Names, Addresses, and the DNS

## 1.4 Internets, Intranets, and Extranets

## 1.5 Designing Applications

### 1.5.1 Client/Server

### 1.5.2 Peer-to-Peer

### 1.5.3 Application Programming Interfaces (APIs)

## 1.6 Standardization Process

### 1.6.1 Request for Comments (RFC)

### 1.6.2 Other Standards

## 1.7 Implementations and Software Distributions

## 1.8 Attacks Involving the Internet Architecture

## 1.9 Summary

## 1.10 References

# Chapter 2 The Internet Address Architecture

## 2.1 Introduction

## 2.2 Expressing IP Addresses

ipv4: 4\*8 = 32

ipv6: 8\*16 = 128

ipv6 写法标准:

1. 一个块中前导的零不必书写。在前面的例子中，地址可写为 5f05:2000:80ad:5800:58:800:2023:1d71。 
2. 全零的块可以省略，并用符号：代替。例如，IPv6 地址0:0:0:0:0:0:0:1可简写为 ::1.  同样，地址 2001:0db8:0:0:0:0:0:2可简写为 2001:db8::2。为了避免出现歧义，一个 IPv6 地址 中符号 :: 只能使用一次。 
3. 在IPv6 格式中嵌入IPv4 地址可使用混合符号形式，紧接着 IPv4 部分的地址块的值为ffff，地址的其余部分使用点分四组格式。例如，IPv6 地址 ::ffff:10.0.0.1可表示 IPv4 地址 10.0.0.1。它被称为IPv4 映射的 IPv6 地址。 
4. IPv6 地址的低 32 位通常采用点分四组表示法。因此，IPv6 地址 ::0102:f001 相当于地址：::1.2.240.1。它被称为IPv4 兼容的 IPv6 地址。需要注意，IPv4 兼容地址与IPv4 映射地址不同；它们只是在能用类似 IPv4 地址的方式书写或由软件处理方面给人以兼容的感觉。这种地 址最初用于 IPv4 和 IPv6 之间的过渡计划，但现在不再需要 [RFC4291]。
5. 前导的零必须压缩（例如，2001:0db8::0022变成 2001:db8::22)
6. :: 只能用于影响最大的地方（压缩最多的零)，但并不只是针对16位的块。如果多个块中包含等长度的零，顺序靠前的块将被替换为 ::
7. a 到 f 的十六进制数字应该用小写表示。 

在大多数情况下，我们会遵守这些规则。

## 2.3 Basic IP Address Structure

### 2.3.1 Classful Addressing

(192 是 C 类地址)

ABC 用于单播地址

有几个地址通常不作为单播地址使用, 特别是第一个和最后一个, 一般要-2

![截屏2022-12-27 13.32.26](https://tva1.sinaimg.cn/large/008vxvgGly1h9ib4d26ecj30v00i2wfz.jpg)

### 2.3.2 Subnet Addressing

将主机号划分为子网 id 和主机 id

### 2.3.3 Subnet Masks

子网掩码用来划分子网id和主机id

外部 router 不关心子网掩码

### 2.3.4 Variable-Length Subnet Masks (VLSM)

每个子网可以使用不同长度的子网掩码

### 2.3.5 Broadcast Addresses

(子网广播地址)

即网络id 子网 id 不变, 将主机 id 全部设置为 1

但是这种定向广播是又问同样的, 在 internet 中被禁用

本地网络广播; 255.255.255.255, 不会被路由器转发, 但是同一网络中的其他主机会收到

### 2.3.6 IPv6 Addresses and Interface Identifiers

## 2.4 CIDR(Classless Inter-Domain Routing) and Aggregation

为了解决两个问题: ip 不足, 以及路由表过大

### 2.4.1 Prefixes

类似 VLSM, CIDR掩码可以采用任意长度,  这个掩码是全球路由系统可见的, 这个又叫网络前缀

### 2.4.2 Aggregation 聚合

分层路由: ip 地址与路由器的拓扑位置有关

在 internet 中, 通过将相邻的多个 ip 前缀合并为一个短前缀的过程叫做聚合

## 2.5 Special-Use Addresses

0.0.0.0/8 本地主机

127.0.0.1 主机回送地址

172.16.0.0/12, 192.168.0.0/16专用网络, 内联网地址, 不会出现在公共网中

255.255.255.255/32 本地网络广播地址

### 2.5.1 Addressing IPv4/IPv6 Translators

嵌入 ipv4 的 ipv6 地址

### 2.5.2 Multicast Addresses

ASM 任意源组播

SSM 特定组播, 每个组只使用一个方发送方

### 2.5.3 IPv4 Multicast Addresses

### 2.5.4 IPv6 Multicast Addresses

### 2.5.5 Anycast Addresses

## 2.6 Allocation

### 2.6.1 Unicast

RIR(Regional Internet Registry) -> ISP -> 客户

- PA 供应商聚合
- PI 供应商独立

供应商倾向使用 PA, 因为可以进行聚合减小路由表, PI 一般需要额外收费

### 2.6.2 Multicast

## 2.7 Unicast Address Assignment

### 2.7.1 Single Provider/No Network/Single Address

单设备

### 2.7.2 Single Provider/Single Network/Single Address

LAN: 路由器

### 2.7.3 Single Provider/Multiple Networks/Multiple Addresses

DMZ(demilitarized zone)

### 2.7.4 Multiple Providers/Multiple Networks/Multiple Addresses (Multihoming)

## 2.8 Attacks Involving IP Addresses

## 2.9 Summary

## 2.10 References

# Chapter 3 Link Layer

## 3.1 Introduction

## 3.2 Ethernet and the IEEE 802 LAN/MAN Standards

### 3.2.1 The IEEE 802 LAN/MAN Standards

### 3.2.2 The Ethernet Frame Format

#### 3.2.3 802.1p/q: Virtual LANs and QoS Tagging

##### 3.2.4 802.1AX: Link Aggregation (Formerly 802.3ad)

### 3.3 Full Duplex, Power Save, Autonegotiation, and 802.1X Flow Control

### 3.3.1 Duplex Mismatch

### 3.3.2 Wake-on LAN (WoL), Power Saving, and Magic Packets

### 3.3.3 Link-Layer Flow Control

## 3.4 Bridges and Switches

### 3.4.1 Spanning Tree Protocol (STP)

#### 3.4.2 802.1ak: Multiple Registration Protocol (MRP)

### 3.5 Wireless LANs—IEEE 802.11(Wi-Fi)

#### 3.5.1 802.11 Frames

### 3.5.2 Power Save Mode and the Time Sync Function (TSF)

#### 3.5.3 802.11 Media Access Control

### 3.5.4 Physical-Layer Details: Rates, Channels, and Frequencies

### 3.5.5 Wi-Fi Security

#### 3.5.6 Wi-Fi Mesh (802.11s)

## 3.6 Point-to-Point Protocol (PPP)

### 3.6.1 Link Control Protocol (LCP)

### 3.6.2 Multilink PPP (MP)

### 3.6.3 Compression Control Protocol (CCP)

### 3.6.4 PPP Authentication

### 3.6.5 Network Control Protocols (NCPs)

### 3.6.6 Header Compression

### 3.6.7 Example

## 3.7 Loopback

## 3.8 MTU and Path MTU

## 3.9 Tunneling Basics

### 3.9.1 Unidirectional Links

## 3.10 Attacks on the Link Layer

## 3.11 Summary

## 3.12 References

# Chapter 4 ARP: Address Resolution Protocol

## 4.1 Introduction

## 4.2 An Example

### 4.2.1 Direct Delivery and ARP

## 4.3 ARP Cache

## 4.4 ARP Frame Format

## 4.5 ARP Examples

### 4.5.1 Normal Example

### 4.5.2 ARP Request to a Nonexistent Host

## 4.6 ARP Cache Timeout

## 4.7 Proxy ARP

## 4.8 Gratuitous ARP and Address Conflict Detection (ACD)

## 4.9 The arp Command

## 4.10 Using ARP to Set an Embedded Device’s IPv4 Address

## 4.11 Attacks Involving ARP

## 4.12 Summary

## 4.13 References

# Chapter 5 The Internet Protocol (IP)

## 5.1 Introduction

## 5.2 IPv4 and IPv6 Headers

### 5.2.1 IP Header Fields

### 5.2.2 The Internet Checksum

### 5.2.3 DS Field and ECN (Formerly Called the ToS Byte or IPv6 Traffic Class)

### 5.2.4 IP Options

## 5.3 IPv6 Extension Headers

### 5.3.1 IPv6 Options

### 5.3.2 Routing Header

### 5.3.3 Fragment Header

## 5.4 IP Forwarding

### 5.4.1 Forwarding Table

### 5.4.2 IP Forwarding Actions

### 5.4.3 Examples

### 5.4.4 Discussion

## 5.5 Mobile IP

### 5.5.1 The Basic Model: Bidirectional Tunneling

### 5.5.2 Route Optimization (RO)

### 5.5.3 Discussion

## 5.6 Host Processing of IP Datagrams

### 5.6.1 Host Models

### 5.6.2 Address Selection

## 5.7 Attacks Involving IP

## 5.8 Summary

## 5.9 References

# Chapter 6 System Configuration: DHCP and Autoconfiguration

## 6.1 Introduction

## 6.2 Dynamic Host Configuration Protocol (DHCP)

### 6.2.1 Address Pools and Leases

### 6.2.2 DHCP and BOOTP Message Format

### 6.2.3 DHCP and BOOTP Options

### 6.2.4 DHCP Protocol Operation

### 6.2.5 DHCPv6

### 6.2.6 Using DHCP with Relays

### 6.2.7 DHCP Authentication

### 6.2.8 Reconfigure Extension

### 6.2.9 Rapid Commit

### 6.2.10 Location Information (LCI and LoST)

### 6.2.11 Mobility and Handoff Information (MoS and ANDSF)

### 6.2.12 DHCP Snooping

## 6.3 Stateless Address Autoconfiguration (SLAAC)

### 6.3.1 Dynamic Configuration of IPv4 Link-Local Addresses

### 6.3.2 IPv6 SLAAC for Link-Local Addresses

## 6.4 DHCP and DNS Interaction

## 6.5 PPP over Ethernet (PPPoE)

## 6.6 Attacks Involving System Configuration

## 6.7 Summary

## 6.8 References

# Chapter 7 Firewalls and Network Address Translation (NAT)

## 7.1 Introduction

## 7.2 Firewalls

### 7.2.1 Packet-Filtering Firewalls

### 7.2.2 Proxy Firewalls

## 7.3 Network Address Translation (NAT)

### 7.3.1 Traditional NAT: Basic NAT and NAPT

### 7.3.2 Address and Port Translation Behavior

### 7.3.3 Filtering Behavior

### 7.3.4 Servers behind NATs

### 7.3.5 Hairpinning and NAT Loopback

### 7.3.6 NAT Editors

### 7.3.7 Service Provider NAT (SPNAT) and Service Provider IPv6 Transition

## 7.4 NAT Traversal

### 7.4.1 Pinholes and Hole Punching

### 7.4.2 UNilateral Self-Address Fixing (UNSAF)

### 7.4.3 Session Traversal Utilities for NAT (STUN)

### 7.4.4 Traversal Using Relays around NAT (TURN)

### 7.4.5 Interactive Connectivity Establishment (ICE)

## 7.5 Configuring Packet-Filtering Firewalls and NATs

### 7.5.1 Firewall Rules

### 7.5.2 NAT Rules

### 7.5.3 Direct Interaction with NATs and Firewalls: UPnP, NAT-PMP, and PCP

## 7.6 NAT for IPv4/IPv6 Coexistence and Transition

### 7.6.1 Dual-Stack Lite (DS-Lite)

### 7.6.2 IPv4/IPv6 Translation Using NATs and ALGs

## 7.7 Attacks Involving Firewalls and NATs

## 7.8 Summary

## 7.9 References

# Chapter 8 ICMPv4 and ICMPv6: Internet Control Message Protocol

## 8.1 Introduction

### 8.1.1 Encapsulation in IPv4 and IPv6

## 8.2 ICMP Messages

### 8.2.1 ICMPv4 Messages

### 8.2.2 ICMPv6 Messages

### 8.2.3 Processing of ICMP Messages

## 8.3 ICMP Error Messages

### 8.3.1 Extended ICMP and Multipart Messages

### 8.3.2 Destination Unreachable (ICMPv4 Type 3, ICMPv6 Type 1) and Packet Too Big (ICMPv6 Type 2)

### 8.3.3 Redirect (ICMPv4 Type 5, ICMPv6 Type 137)

### 8.3.4 ICMP Time Exceeded (ICMPv4 Type 11, ICMPv6 Type 3)

### 8.3.5 Parameter Problem (ICMPv4 Type 12, ICMPv6 Type 4)

## 8.4 ICMP Query/Informational Messages

### 8.4.1 Echo Request/Reply (ping) (ICMPv4 Types 0/8, ICMPv6 Types 129/128)

### 8.4.2 Router Discovery: Router Solicitation and Advertisement (ICMPv4 Types 9, 10)

### 8.4.3 Home Agent Address Discovery Request/Reply (ICMPv6 Types 144/145)

### 8.4.4 Mobile Prefix Solicitation/Advertisement (ICMPv6 Types 146/147)

### 8.4.5 Mobile IPv6 Fast Handover Messages (ICMPv6 Type 154)

### 8.4.6 Multicast Listener Query/Report/Done (ICMPv6 Types 130/131/132)

### 8.4.7 Version 2 Multicast Listener Discovery (MLDv2) (ICMPv6 Type 143)

### 8.4.8 Multicast Router Discovery (MRD) (IGMP Types 48/49/50, ICMPv6 Types 151/152/153)

## 8.5 Neighbor Discovery in IPv6

### 8.5.1 ICMPv6 Router Solicitation and Advertisement (ICMPv6 Types 133, 134)

### 8.5.2 ICMPv6 Neighbor Solicitation and Advertisement (IMCPv6 Types 135, 136)

### 8.5.3 ICMPv6 Inverse Neighbor Discovery Solicitation/Advertisement (ICMPv6 Types 141/142)

### 8.5.4 Neighbor Unreachability Detection (NUD)

### 8.5.5 Secure Neighbor Discovery (SEND)

### 8.5.6 ICMPv6 Neighbor Discovery (ND) Options

## 8.6 Translating ICMPv4 and ICMPv6

### 8.6.1 Translating ICMPv4 to ICMPv6

### 8.6.2 Translating ICMPv6 to ICMPv4

## 8.7 Attacks Involving ICMP

## 8.8 Summary

## 8.9 References

# Chapter 9 Broadcasting and Local Multicasting (IGMP and MLD)

## 9.1 Introduction

## 9.2 Broadcasting

### 9.2.1 Using Broadcast Addresses

### 9.2.2 Sending Broadcast Datagrams

## 9.3 Multicasting

### 9.3.1 Converting IP Multicast Addresses to 802 MAC/Ethernet Addresses

### 9.3.2 Examples

### 9.3.3 Sending Multicast Datagrams

### 9.3.4 Receiving Multicast Datagrams

### 9.3.5 Host Address Filtering

## 9.4 The Internet Group Management Protocol (IGMP) and Multicast Listener Discovery Protocol (MLD)

### 9.4.1 IGMP and MLD Processing by Group Members (“Group Member Part”)

### 9.4.2 IGMP and MLD Processing by Multicast Routers (“Multicast Router Part”)

### 9.4.3 Examples

### 9.4.4 Lightweight IGMPv3 and MLDv2

### 9.4.5 IGMP and MLD Robustness

### 9.4.6 IGMP and MLD Counters and Variables

### 9.4.7 IGMP and MLD Snooping

## 9.5 Attacks Involving IGMP and MLD

## 9.6 Summary

## 9.7 References

# Chapter 10 User Datagram Protocol (UDP) and IP Fragmentation

## 10.1 Introduction

## 10.2 UDP Header

## 10.3 UDP Checksum

## 10.4 Examples

## 10.5 UDP and IPv6

### 10.5.1 Teredo: Tunneling IPv6 through IPv4 Networks

## 10.6 UDP-Lite

## 10.7 IP Fragmentation

### 10.7.1 Example: UDP/IPv4 Fragmentation

### 10.7.2 Reassembly Timeout

## 10.8 Path MTU Discovery with UDP

### 10.8.1 Example

## 10.9 Interaction between IP Fragmentation and ARP/ND

## 10.10 Maximum UDP Datagram Size

### 10.10.1 Implementation Limitations

### 10.10.2 Datagram Truncation

## 10.11 UDP Server Design

### 10.11.1 IP Addresses and UDP Port Numbers

### 10.11.2 Restricting Local IP Addresses

### 10.11.3 Using Multiple Addresses

### 10.11.4 Restricting Foreign IP Address

### 10.11.5 Using Multiple Servers per Port

### 10.11.6 Spanning Address Families: IPv4 and IPv6

### 10.11.7 Lack of Flow and Congestion Control

## 10.12 Translating UDP/IPv4 and UDP/IPv6 Datagrams

## 10.13 UDP in the Internet

## 10.14 Attacks Involving UDP and IP Fragmentation

## 10.15 Summary

## 10.16 References

# Chapter 11 Name Resolution and the Domain Name System (DNS)

## 11.1 Introduction

## 11.2 The DNS Name Space

### 11.2.1 DNS Naming Syntax

## 11.3 Name Servers and Zones

## 11.4 Caching

## 11.5 The DNS Protocol

### 11.5.1 DNS Message Format

### 11.5.2 The DNS Extension Format (EDNS0)

### 11.5.3 UDP or TCP

### 11.5.4 Question (Query) and Zone Section Format

### 11.5.5 Answer, Authority, and Additional Information Section Formats

### 11.5.6 Resource Record Types

### 11.5.7 Dynamic Updates (DNS UPDATE)

### 11.5.8 Zone Transfers and DNS NOTIFY

## 11.6 Sort Lists, Round-Robin, and Split DNS

## 11.7 Open DNS Servers and DynDNS

## 11.8 Transparency and Extensibility

## 11.9 Translating DNS from IPv4 to IPv6 (DNS64)

## 11.10 LLMNR and mDNS

## 11.11 LDAP

## 11.12 Attacks on the DNS

## 11.13 Summary

## 11.14 References

# Chapter 12 TCP: The Transmission Control Protocol (Preliminaries)

## 12.1 Introduction

### 12.1.1 ARQ and Retransmission

### 12.1.2 Windows of Packets and Sliding Windows

### 12.1.3 Variable Windows: Flow Control and Congestion Control

### 12.1.4 Setting the Retransmission Timeout

## 12.2 Introduction to TCP

### 12.2.1 The TCP Service Model

### 12.2.2 Reliability in TCP

## 12.3 TCP Header and Encapsulation

## 12.4 Summary

## 12.5 References

# Chapter 13 TCP Connection Management

## 13.1 Introduction

## 13.2 TCP Connection Establishment and Termination

### 13.2.1 TCP Half-Close

### 13.2.2 Simultaneous Open and Close

### 13.2.3 Initial Sequence Number (ISN)

### 13.2.4 Example

### 13.2.5 Timeout of Connection Establishment

### 13.2.6 Connections and Translators

## 13.3 TCP Options

### 13.3.1 Maximum Segment Size (MSS) Option

### 13.3.2 Selective Acknowledgment (SACK) Options

### 13.3.3 Window Scale (WSCALE or WSOPT) Option

### 13.3.4 Timestamps Option and Protection against Wrapped Sequence Numbers (PAWS)

### 13.3.5 User Timeout (UTO) Option

### 13.3.6 Authentication Option (TCP-AO)

## 13.4 Path MTU Discovery with TCP

### 13.4.1 Example

## 13.5 TCP State Transitions

### 13.5.1 TCP State Transition Diagram

### 13.5.2 TIME_WAIT (2MSL Wait) State

### 13.5.3 Quiet Time Concept

### 13.5.4 FIN_WAIT_2 State

### 13.5.5 Simultaneous Open and Close Transitions

## 13.6 Reset Segments

### 13.6.1 Connection Request to Nonexistent Port

### 13.6.2 Aborting a Connection

### 13.6.3 Half-Open Connections

### 13.6.4 TIME-WAIT Assassination (TWA)

## 13.7 TCP Server Operation

### 13.7.1 TCP Port Numbers

### 13.7.2 Restricting Local IP Addresses

### 13.7.3 Restricting Foreign Endpoints

### 13.7.4 Incoming Connection Queue

## 13.8 Attacks Involving TCP Connection Management

## 13.9 Summary

## 13.10 References

# Chapter 14 TCP Timeout and Retransmission

## 14.1 Introduction

## 14.2 Simple Timeout and Retransmission Example

## 14.3 Setting the Retransmission Timeout (RTO)

### 14.3.1 The Classic Method

### 14.3.2 The Standard Method

### 14.3.3 The Linux Method

### 14.3.4 RTT Estimator Behaviors

### 14.3.5 RTTM Robustness to Loss and Reordering

## 14.4 Timer-Based Retransmission

### 14.4.1 Example

## 14.5 Fast Retransmit

### 14.5.1 Example

## 14.6 Retransmission with Selective Acknowledgments

### 14.6.1 SACK Receiver Behavior

### 14.6.2 SACK Sender Behavior

### 14.6.3 Example

## 14.7 Spurious Timeouts and Retransmissions

### 14.7.1 Duplicate SACK (DSACK) Extension

### 14.7.2 The Eifel Detection Algorithm

### 14.7.3 Forward-RTO Recovery (F-RTO)

### 14.7.4 The Eifel Response Algorithm

## 14.8 Packet Reordering and Duplication

### 14.8.1 Reordering

### 14.8.2 Duplication

## 14.9 Destination Metrics

## 14.10 Repacketization

## 14.11 Attacks Involving TCP Retransmission

## 14.12 Summary

## 14.13 References

# Chapter 15 TCP Data Flow and Window Management

## 15.1 Introduction

## 15.2 Interactive Communication

## 15.3 Delayed Acknowledgments

## 15.4 Nagle Algorithm

### 15.4.1 Delayed ACK and Nagle Algorithm Interaction

### 15.4.2 Disabling the Nagle Algorithm

## 15.5 Flow Control and Window Management

### 15.5.1 Sliding Windows

### 15.5.2 Zero Windows and the TCP Persist Timer

### 15.5.3 Silly Window Syndrome (SWS)

### 15.5.4 Large Buffers and Auto-Tuning

## 15.6 Urgent Mechanism

### 15.6.1 Example

## 15.7 Attacks Involving Window Management

## 15.8 Summary

## 15.9 References

# Chapter 16 TCP Congestion Control

## 16.1 Introduction

### 16.1.1 Detection of Congestion in TCP

### 16.1.2 Slowing Down a TCP Sender

## 16.2 The Classic Algorithms

### 16.2.1 Slow Start

### 16.2.2 Congestion Avoidance

### 16.2.3 Selecting between Slow Start and Congestion Avoidance

### 16.2.4 Tahoe, Reno, and Fast Recovery

### 16.2.5 Standard TCP

## 16.3 Evolution of the Standard Algorithms

### 16.3.1 NewReno

### 16.3.2 TCP Congestion Control with SACK

### 16.3.3 Forward Acknowledgment (FACK) and Rate Halving

### 16.3.4 Limited Transmit

### 16.3.5 Congestion Window Validation (CWV)

## 16.4 Handling Spurious RTOs—the Eifel Response Algorithm

## 16.5 An Extended Example

### 16.5.1 Slow Start Behavior

### 16.5.2 Sender Pause and Local Congestion (Event 1)

### 16.5.3 Stretch ACKs and Recovery from Local Congestion

### 16.5.4 Fast Retransmission and SACK Recovery (Event 2)

### 16.5.5 Additional Local Congestion and Fast Retransmit Events

### 16.5.6 Timeouts, Retransmissions, and Undoing cwnd Changes

### 16.5.7 Connection Completion

## 16.6 Sharing Congestion State

## 16.7 TCP Friendliness

## 16.8 TCP in High-Speed Environments

### 16.8.1 HighSpeed TCP (HSTCP) and Limited Slow Start

### 16.8.2 Binary Increase Congestion Control (BIC and CUBIC)

## 16.9 Delay-Based Congestion Control

### 16.9.1 Vegas

### 16.9.2 FAST

### 16.9.3 TCP Westwood and Westwood+

### 16.9.4 Compound TCP

## 16.10 Buffer Bloat

## 16.11 Active Queue Management and ECN

## 16.12 Attacks Involving TCP Congestion Control

## 16.13 Summary

## 16.14 References

# Chapter 17 TCP Keepalive

## 17.1 Introduction

## 17.2 Description

### 17.2.1 Keepalive Examples

## 17.3 Attacks Involving TCP Keepalives

## 17.4 Summary

## 17.5 References

# Chapter 18 Security: EAP, IPsec, TLS, DNSSEC, and DKIM

## 18.1 Introduction

## 18.2 Basic Principles of Information Security

## 18.3 Threats to Network Communication

## 18.4 Basic Cryptography and Security Mechanisms

### 18.4.1 Cryptosystems

### 18.4.2 Rivest, Shamir, and Adleman (RSA) Public Key Cryptography

### 18.4.3 Diffie-Hellman-Merkle Key Agreement (aka Diffie-Hellman or DH)

### 18.4.4 Signcryption and Elliptic Curve Cryptography (ECC)

### 18.4.5 Key Derivation and Perfect Forward Secrecy (PFS)

### 18.4.6 Pseudorandom Numbers, Generators, and Function Families

### 18.4.7 Nonces and Salt

### 18.4.8 Cryptographic Hash Functions and Message Digests

### 18.4.9 Message Authentication Codes (MACs, HMAC, CMAC, and GMAC)

### 18.4.10 Cryptographic Suites and Cipher Suites

## 18.5 Certificates, Certificate Authorities (CAs), and PKIs

#### 18.5.1 Public Key Certificates, Certificate Authorities, and X.509

### 18.5.2 Validating and Revoking Certificates

### 18.5.3 Attribute Certificates

## 18.6 TCP/IP Security Protocols and Layering

#### 18.7 Network Access Control: 802.1X, 802.1AE, EAP, and PANA

### 18.7.1 EAP Methods and Key Derivation

### 18.7.2 The EAP Re-authentication Protocol (ERP)

### 18.7.3 Protocol for Carrying Authentication for Network Access (PANA)

## 18.8 Layer 3 IP Security (IPsec)

### 18.8.1 Internet Key Exchange (IKEv2) Protocol

### 18.8.2 Authentication Header (AH)

### 18.8.3 Encapsulating Security Payload (ESP)

### 18.8.4 Multicast

### 18.8.5 L2TP/IPsec

### 18.8.6 IPsec NAT Traversal

### 18.8.7 Example

## 18.9 Transport Layer Security (TLS and DTLS)

#### 18.9.1 TLS 1.2

### 18.9.2 TLS with Datagrams (DTLS)

## 18.10 DNS Security (DNSSEC)

### 18.10.1 DNSSEC Resource Records

### 18.10.2 DNSSEC Operation

### 18.10.3 Transaction Authentication (TSIG, TKEY, and SIG(0))

### 18.10.4 DNSSEC with DNS64

## 18.11 DomainKeys Identified Mail (DKIM)

### 18.11.1 DKIM Signatures

### 18.11.2 Example

## 18.12 Attacks on Security Protocols

## 18.13 Summary

## 18.14 References

# 其他

# internet www difference

| S.No. | INTERNET                                                                                  | WWW                                                                                     |
|:----- |:----------------------------------------------------------------------------------------- |:--------------------------------------------------------------------------------------- |
| 1     | Internet is a global network of networks.                                                 | WWW stands for World wide Web.                                                          |
| 2     | Internet is a means of connecting a computer to any other computer anywhere in the world. | World Wide Web which is a collection of information which is accessed via the Internet. |
| 3     | Internet is infrastructure.                                                               | WWW is **service** on top of that infrastructure.                                       |
| 4     | Internet can be viewed as a big book-store.                                               | Web can be viewed as collection of books on that store.                                 |
| 5     | At some advanced level, to understand we can think of the Internet as hardware.           | At some advanced level, to understand we can think of the WWW as software.              |
| 6     | Internet is primarily hardware-based.                                                     | WWW is more software-oriented as compared to the Internet.                              |
| 7     | It is originated sometimes in late 1960s.                                                 | English scientist Tim Berners-Lee invented the World Wide Web in 1989.                  |
| 8     | Internet is superset of WWW.                                                              | WWW is a subset of the Internet.                                                        |
| 9     | The first version of the Internet was known as ARPANET.                                   | In the beginning WWW was known as NSFNET.                                               |
| 10    | Internet uses IP address.                                                                 | WWW uses HTTP.                                                                          |
