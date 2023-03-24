# Hardware specifications

Neuron is fully developed in C language and supports running on X86, ARM, MIPS, RISC-V and other hardware architectures as well as container deployment, such as K8s, KubeEdge, etc. On devices with limited hardware resources, it can also achieve data acquisition of 100 ms or even 10 ms level. On servers with sufficient hardware resources, Neuron can also make full use of multi-core CPUs, and can simultaneously conduct data acquisition and point write control of hundreds of thousands of points at the frequency of 100 ms.

The following table lists the hardware conditions required for the minimum demand of Neuron at different number of tags.

|Specifications|Minimum configuration recommendation|Hardware architecture|remarks|
| :-------------------- | :------------------------------ | :---------------------------------- | :----------------------------------- |
| 100 tags | 128M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Small gateway device |
| 1,000 tags | 256M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway device |
| 10,000 tags | 512M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway, industrial computer, etc |
| More than 10,000 tags | 1G memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium or large gateway, industrial computer, servers, etc |
