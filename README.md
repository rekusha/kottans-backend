<p>Alexandr Rekun and there is my kottans-backend</p>
<p>## Git Basics</p>
<p>## Unix Shell</p>
<p>## Git Collaboration</p>


<h2>Task 1. ## Git Basics - #done</h2>
<p><img src="/Git_intro/Git_intro_done.png" alt="task1_done"/></p>
<p></p>
<h2>Task 2. ## Unix Shell - #done</h2>
<p>Like the good old dos but more advanced</p>
<p><img src="/Unix_shell/linuxsurvival_quiz_1.png" alt="task2_done"/></p>
<p><img src="/Unix_shell/linuxsurvival_quiz_2.png" alt="task2_done"/></p>
<p><img src="/Unix_shell/linuxsurvival_quiz_3.png" alt="task2_done"/></p>
<p><img src="/Unix_shell/linuxsurvival_quiz_4.png" alt="task2_done"/></p>

<h2>Task 3. ## Git Collaboration - #done</h2>
<p>Now i'm can delete my repository with more powerful tool! )</p>
<p><img src="/task_git_collaboration/git_collaboration.png" alt="task3_done"/></p>

<h2>Task 4. ## Python Basics 1 - #done</h2>
<p>link to HackerRank profile - https://www.hackerrank.com/rekusha</p>

<h2>Task 5. ## Memory Management - #done</h2>
<p>add answers to the following questions:</p>
<p>What's going to happen if program reaches maximum limit of stack?</p>
<p>we have a <i>stack overflow</i> and the program receives a <i>segmentation fault</i></p>
<p></p>
<p>What's going to happen if program requests a big (more then 128KB) memory allocation on heap?</p>
<p>will create an <i>anonymous memory mapping</i></p>
<p></p>
<p>What's the difference between Text and Data memory segments?</p>
<p>Read/Write area. data segment holds the contents for static and global variables initialized in source code.</p>
<p>Read/Exacute area. text segment stores all of the code and literals. text segment maps binary file in memory. Segmentation Fault if try to write to this area.</p>
<p></p>
<details>
<pre>00400000-00421000 r--p 00000000 08:11 3671085                            /usr/bin/python3.7
00421000-00655000 r-xp 00021000 08:11 3671085                            /usr/bin/python3.7
00655000-00801000 r--p 00255000 08:11 3671085                            /usr/bin/python3.7
00801000-00802000 r--p 00400000 08:11 3671085                            /usr/bin/python3.7
00802000-008a8000 rw-p 00401000 08:11 3671085                            /usr/bin/python3.7
008a8000-008cb000 rw-p 00000000 00:00 0 
011ac000-01487000 rw-p 00000000 00:00 0                                  [heap]
7fe2a3c2e000-7fe2a3d7f000 rw-p 00000000 00:00 0 
7fe2a3d7f000-7fe2a3d83000 r--p 00000000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3d83000-7fe2a3d96000 r-xp 00004000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3d96000-7fe2a3d9f000 r--p 00017000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3d9f000-7fe2a3da0000 ---p 00020000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3da0000-7fe2a3da1000 r--p 00020000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3da1000-7fe2a3da2000 rw-p 00021000 08:11 3678628                    /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.26.1
7fe2a3da2000-7fe2a3dae000 r--p 00000000 08:11 3678558                    /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.4
7fe2a3dae000-7fe2a3e7b000 r-xp 0000c000 08:11 3678558                    /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.4
7fe2a3e7b000-7fe2a3eb8000 r--p 000d9000 08:11 3678558                    /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.4
7fe2a3eb8000-7fe2a3eba000 r--p 00115000 08:11 3678558                    /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.4
7fe2a3eba000-7fe2a3ebf000 rw-p 00117000 08:11 3678558                    /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.4
7fe2a3ebf000-7fe2a3ece000 r--p 00000000 08:11 3670112                    /usr/lib/x86_64-linux-gnu/libsystemd.so.0.24.0
7fe2a3ece000-7fe2a3f37000 r-xp 0000f000 08:11 3670112                    /usr/lib/x86_64-linux-gnu/libsystemd.so.0.24.0
7fe2a3f37000-7fe2a3f58000 r--p 00078000 08:11 3670112                    /usr/lib/x86_64-linux-gnu/libsystemd.so.0.24.0
7fe2a3f58000-7fe2a3f5b000 r--p 00098000 08:11 3670112                    /usr/lib/x86_64-linux-gnu/libsystemd.so.0.24.0
7fe2a3f5b000-7fe2a3f5c000 rw-p 0009b000 08:11 3670112                    /usr/lib/x86_64-linux-gnu/libsystemd.so.0.24.0
7fe2a3f5c000-7fe2a3f5d000 rw-p 00000000 00:00 0 
7fe2a3f5d000-7fe2a3f61000 r--p 00000000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f61000-7fe2a3f78000 r-xp 00004000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f78000-7fe2a3f80000 r--p 0001b000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f80000-7fe2a3f81000 ---p 00023000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f81000-7fe2a3f82000 r--p 00023000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f82000-7fe2a3f83000 rw-p 00024000 08:11 3670577                    /usr/lib/x86_64-linux-gnu/libudev.so.1.6.12
7fe2a3f83000-7fe2a3f87000 r--p 00000000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a3f87000-7fe2a400f000 r-xp 00004000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a400f000-7fe2a401f000 r--p 0008c000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a401f000-7fe2a4020000 ---p 0009c000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a4020000-7fe2a4021000 r--p 0009c000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a4021000-7fe2a4022000 rw-p 0009d000 08:11 3679577                    /usr/lib/x86_64-linux-gnu/libzstd.so.1.3.8
7fe2a4022000-7fe2a4024000 r--p 00000000 08:11 3678883                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.8.3
7fe2a4024000-7fe2a404c000 r-xp 00002000 08:11 3678883                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.8.3
7fe2a404c000-7fe2a404f000 r--p 0002a000 08:11 3678883                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.8.3
7fe2a404f000-7fe2a4050000 r--p 0002c000 08:11 3678883                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.8.3
7fe2a4050000-7fe2a4051000 rw-p 0002d000 08:11 3678883                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.8.3
7fe2a4051000-7fe2a4055000 r--p 00000000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a4055000-7fe2a4064000 r-xp 00004000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a4064000-7fe2a4067000 r--p 00013000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a4067000-7fe2a4068000 ---p 00016000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a4068000-7fe2a4069000 r--p 00016000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a4069000-7fe2a406a000 rw-p 00017000 08:11 3679204                    /usr/lib/x86_64-linux-gnu/libresolv-2.29.so
7fe2a406a000-7fe2a406c000 rw-p 00000000 00:00 0 
7fe2a406c000-7fe2a406f000 r--p 00000000 08:11 3670202                    /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
7fe2a406f000-7fe2a4080000 r-xp 00003000 08:11 3670202                    /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
7fe2a4080000-7fe2a4084000 r--p 00014000 08:11 3670202                    /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
7fe2a4084000-7fe2a4085000 r--p 00017000 08:11 3670202                    /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
7fe2a4085000-7fe2a4086000 rw-p 00018000 08:11 3670202                    /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
7fe2a4086000-7fe2a411b000 r--p 00000000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a411b000-7fe2a420d000 r-xp 00095000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a420d000-7fe2a4256000 r--p 00187000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a4256000-7fe2a4257000 ---p 001d0000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a4257000-7fe2a4262000 r--p 001d0000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a4262000-7fe2a4265000 rw-p 001db000 08:11 3670452                    /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26
7fe2a4265000-7fe2a4268000 rw-p 00000000 00:00 0 
7fe2a4268000-7fe2a42ac000 r--p 00000000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a42ac000-7fe2a43e4000 r-xp 00044000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a43e4000-7fe2a442b000 r--p 0017c000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a442b000-7fe2a442c000 ---p 001c3000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a442c000-7fe2a4432000 r--p 001c3000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a4432000-7fe2a4433000 rw-p 001c9000 08:11 3670156                    /usr/lib/x86_64-linux-gnu/libapt-pkg.so.5.0.2
7fe2a4433000-7fe2a444a000 r--p 00000000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a444a000-7fe2a4468000 r-xp 00017000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a4468000-7fe2a447f000 r--p 00035000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a447f000-7fe2a4480000 ---p 0004c000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a4480000-7fe2a4482000 r--p 0004c000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a4482000-7fe2a448b000 rw-p 0004e000 08:11 4065692                    /usr/lib/python3/dist-packages/apt_pkg.cpython-37m-x86_64-linux-gnu.so
7fe2a448b000-7fe2a454b000 rw-p 00000000 00:00 0 
7fe2a454b000-7fe2a4567000 r--p 00000000 08:11 3677937                    /usr/lib/x86_64-linux-gnu/libssl.so.1.1
7fe2a4567000-7fe2a45b4000 r-xp 0001c000 08:11 3677937                    /usr/lib/x86_64-linux-gnu/libssl.so.1.1
7fe2a45b4000-7fe2a45ce000 r--p 00069000 08:11 3677937                    /usr/lib/x86_64-linux-gnu/libssl.so.1.1
7fe2a45ce000-7fe2a45d7000 r--p 00082000 08:11 3677937                    /usr/lib/x86_64-linux-gnu/libssl.so.1.1
7fe2a45d7000-7fe2a45db000 rw-p 0008b000 08:11 3677937                    /usr/lib/x86_64-linux-gnu/libssl.so.1.1
7fe2a45db000-7fe2a45e4000 r--p 00000000 08:11 3807275                    /usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
7fe2a45e4000-7fe2a45ec000 r-xp 00009000 08:11 3807275                    /usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
7fe2a45ec000-7fe2a45f2000 r--p 00011000 08:11 3807275                    /usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
7fe2a45f2000-7fe2a45f3000 r--p 00016000 08:11 3807275                    /usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
7fe2a45f3000-7fe2a45f8000 rw-p 00017000 08:11 3807275                    /usr/lib/python3.7/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
7fe2a45f8000-7fe2a47f8000 rw-p 00000000 00:00 0 
7fe2a47f8000-7fe2a4870000 r--p 00000000 08:11 3677934                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
7fe2a4870000-7fe2a4a08000 r-xp 00078000 08:11 3677934                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
7fe2a4a08000-7fe2a4a95000 r--p 00210000 08:11 3677934                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
7fe2a4a95000-7fe2a4ac1000 r--p 0029c000 08:11 3677934                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
7fe2a4ac1000-7fe2a4ac3000 rw-p 002c8000 08:11 3677934                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
7fe2a4ac3000-7fe2a4ac6000 rw-p 00000000 00:00 0 
7fe2a4acf000-7fe2a4b0f000 rw-p 00000000 00:00 0 
7fe2a4b0f000-7fe2a4b12000 r--p 00000000 08:11 3678885                    /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
7fe2a4b12000-7fe2a4b29000 r-xp 00003000 08:11 3678885                    /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
7fe2a4b29000-7fe2a4b34000 r--p 0001a000 08:11 3678885                    /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
7fe2a4b34000-7fe2a4b35000 r--p 00024000 08:11 3678885                    /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
7fe2a4b35000-7fe2a4b36000 rw-p 00025000 08:11 3678885                    /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
7fe2a4b52000-7fe2a4b54000 r--p 00000000 08:11 3670146                    /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4
7fe2a4b54000-7fe2a4b61000 r-xp 00002000 08:11 3670146                    /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4
7fe2a4b61000-7fe2a4b63000 r--p 0000f000 08:11 3670146                    /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4
7fe2a4b63000-7fe2a4b64000 r--p 00010000 08:11 3670146                    /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4
7fe2a4b64000-7fe2a4b65000 rw-p 00011000 08:11 3670146                    /usr/lib/x86_64-linux-gnu/libbz2.so.1.0.4
7fe2a4b65000-7fe2a4ca5000 rw-p 00000000 00:00 0 
7fe2a4ca5000-7fe2a4cb3000 r--p 00000000 08:11 3679365                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.1
7fe2a4cb3000-7fe2a4cc1000 r-xp 0000e000 08:11 3679365                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.1
7fe2a4cc1000-7fe2a4cce000 r--p 0001c000 08:11 3679365                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.1
7fe2a4cce000-7fe2a4cd2000 r--p 00028000 08:11 3679365                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.1
7fe2a4cd2000-7fe2a4cd3000 rw-p 0002c000 08:11 3679365                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.1
7fe2a4cd3000-7fe2a4ce7000 r--p 00000000 08:11 3679198                    /usr/lib/x86_64-linux-gnu/libreadline.so.8.0
7fe2a4ce7000-7fe2a4d0f000 r-xp 00014000 08:11 3679198                    /usr/lib/x86_64-linux-gnu/libreadline.so.8.0
7fe2a4d0f000-7fe2a4d19000 r--p 0003c000 08:11 3679198                    /usr/lib/x86_64-linux-gnu/libreadline.so.8.0
7fe2a4d19000-7fe2a4d1b000 r--p 00045000 08:11 3679198                    /usr/lib/x86_64-linux-gnu/libreadline.so.8.0
7fe2a4d1b000-7fe2a4d21000 rw-p 00047000 08:11 3679198                    /usr/lib/x86_64-linux-gnu/libreadline.so.8.0
7fe2a4d21000-7fe2a4d22000 rw-p 00000000 00:00 0 
7fe2a4d34000-7fe2a4d36000 r--p 00000000 08:11 3811896                    /usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
7fe2a4d36000-7fe2a4d39000 r-xp 00002000 08:11 3811896                    /usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
7fe2a4d39000-7fe2a4d3b000 r--p 00005000 08:11 3811896                    /usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
7fe2a4d3b000-7fe2a4d3c000 r--p 00006000 08:11 3811896                    /usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
7fe2a4d3c000-7fe2a4d3e000 rw-p 00007000 08:11 3811896                    /usr/lib/python3.7/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
7fe2a4d3e000-7fe2a4d7e000 rw-p 00000000 00:00 0 
7fe2a4d7e000-7fe2a4d81000 r--p 00000000 08:11 3679225                    /usr/lib/x86_64-linux-gnu/librt-2.29.so
7fe2a4d81000-7fe2a4d85000 r-xp 00003000 08:11 3679225                    /usr/lib/x86_64-linux-gnu/librt-2.29.so
7fe2a4d85000-7fe2a4d87000 r--p 00007000 08:11 3679225                    /usr/lib/x86_64-linux-gnu/librt-2.29.so
7fe2a4d87000-7fe2a4d88000 r--p 00008000 08:11 3679225                    /usr/lib/x86_64-linux-gnu/librt-2.29.so
7fe2a4d88000-7fe2a4d89000 rw-p 00009000 08:11 3679225                    /usr/lib/x86_64-linux-gnu/librt-2.29.so
7fe2a4d89000-7fe2a4d8b000 r--p 00000000 08:11 3811894                    /usr/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
7fe2a4d8b000-7fe2a4d96000 r-xp 00002000 08:11 3811894                    /usr/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
7fe2a4d96000-7fe2a4d98000 r--p 0000d000 08:11 3811894                    /usr/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
7fe2a4d98000-7fe2a4d99000 r--p 0000e000 08:11 3811894                    /usr/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
7fe2a4d99000-7fe2a4d9a000 rw-p 0000f000 08:11 3811894                    /usr/lib/python3.7/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
7fe2a4d9a000-7fe2a4d9c000 r--p 00000000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4d9c000-7fe2a4d9f000 r-xp 00002000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4d9f000-7fe2a4da0000 r--p 00005000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4da0000-7fe2a4da1000 ---p 00006000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4da1000-7fe2a4da2000 r--p 00006000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4da2000-7fe2a4da3000 rw-p 00007000 08:11 3807273                    /usr/lib/python3.7/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
7fe2a4da3000-7fe2a4ee3000 rw-p 00000000 00:00 0 
7fe2a4ee3000-7fe2a5f7f000 r--p 00000000 08:11 3677201                    /usr/lib/locale/locale-archive
7fe2a5f7f000-7fe2a5f82000 rw-p 00000000 00:00 0 
7fe2a5f82000-7fe2a5f91000 r--p 00000000 08:11 3678889                    /usr/lib/x86_64-linux-gnu/libm-2.29.so
7fe2a5f91000-7fe2a6037000 r-xp 0000f000 08:11 3678889                    /usr/lib/x86_64-linux-gnu/libm-2.29.so
7fe2a6037000-7fe2a60ce000 r--p 000b5000 08:11 3678889                    /usr/lib/x86_64-linux-gnu/libm-2.29.so
7fe2a60ce000-7fe2a60cf000 r--p 0014b000 08:11 3678889                    /usr/lib/x86_64-linux-gnu/libm-2.29.so
7fe2a60cf000-7fe2a60d0000 rw-p 0014c000 08:11 3678889                    /usr/lib/x86_64-linux-gnu/libm-2.29.so
7fe2a60d0000-7fe2a60d2000 rw-p 00000000 00:00 0 
7fe2a60d2000-7fe2a60d4000 r--p 00000000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60d4000-7fe2a60e5000 r-xp 00002000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60e5000-7fe2a60eb000 r--p 00013000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60eb000-7fe2a60ec000 ---p 00019000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60ec000-7fe2a60ed000 r--p 00019000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60ed000-7fe2a60ee000 rw-p 0001a000 08:11 3679575                    /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
7fe2a60ee000-7fe2a60f2000 r--p 00000000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a60f2000-7fe2a6113000 r-xp 00004000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a6113000-7fe2a6127000 r--p 00025000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a6127000-7fe2a6128000 ---p 00039000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a6128000-7fe2a612a000 r--p 00039000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a612a000-7fe2a612b000 rw-p 0003b000 08:11 3680769                    /usr/lib/x86_64-linux-gnu/libexpat.so.1.6.8
7fe2a612b000-7fe2a612c000 r--p 00000000 08:11 3679422                    /usr/lib/x86_64-linux-gnu/libutil-2.29.so
7fe2a612c000-7fe2a612d000 r-xp 00001000 08:11 3679422                    /usr/lib/x86_64-linux-gnu/libutil-2.29.so
7fe2a612d000-7fe2a612e000 r--p 00002000 08:11 3679422                    /usr/lib/x86_64-linux-gnu/libutil-2.29.so
7fe2a612e000-7fe2a612f000 r--p 00002000 08:11 3679422                    /usr/lib/x86_64-linux-gnu/libutil-2.29.so
7fe2a612f000-7fe2a6130000 rw-p 00003000 08:11 3679422                    /usr/lib/x86_64-linux-gnu/libutil-2.29.so
7fe2a6130000-7fe2a6131000 r--p 00000000 08:11 3678407                    /usr/lib/x86_64-linux-gnu/libdl-2.29.so
7fe2a6131000-7fe2a6133000 r-xp 00001000 08:11 3678407                    /usr/lib/x86_64-linux-gnu/libdl-2.29.so
7fe2a6133000-7fe2a6134000 r--p 00003000 08:11 3678407                    /usr/lib/x86_64-linux-gnu/libdl-2.29.so
7fe2a6134000-7fe2a6135000 r--p 00003000 08:11 3678407                    /usr/lib/x86_64-linux-gnu/libdl-2.29.so
7fe2a6135000-7fe2a6136000 rw-p 00004000 08:11 3678407                    /usr/lib/x86_64-linux-gnu/libdl-2.29.so
7fe2a6136000-7fe2a613d000 r--p 00000000 08:11 3679159                    /usr/lib/x86_64-linux-gnu/libpthread-2.29.so
7fe2a613d000-7fe2a614c000 r-xp 00007000 08:11 3679159                    /usr/lib/x86_64-linux-gnu/libpthread-2.29.so
7fe2a614c000-7fe2a6151000 r--p 00016000 08:11 3679159                    /usr/lib/x86_64-linux-gnu/libpthread-2.29.so
7fe2a6151000-7fe2a6152000 r--p 0001a000 08:11 3679159                    /usr/lib/x86_64-linux-gnu/libpthread-2.29.so
7fe2a6152000-7fe2a6153000 rw-p 0001b000 08:11 3679159                    /usr/lib/x86_64-linux-gnu/libpthread-2.29.so
7fe2a6153000-7fe2a6157000 rw-p 00000000 00:00 0 
7fe2a6157000-7fe2a617c000 r--p 00000000 08:11 3678270                    /usr/lib/x86_64-linux-gnu/libc-2.29.so
7fe2a617c000-7fe2a62ef000 r-xp 00025000 08:11 3678270                    /usr/lib/x86_64-linux-gnu/libc-2.29.so
7fe2a62ef000-7fe2a6338000 r--p 00198000 08:11 3678270                    /usr/lib/x86_64-linux-gnu/libc-2.29.so
7fe2a6338000-7fe2a633b000 r--p 001e0000 08:11 3678270                    /usr/lib/x86_64-linux-gnu/libc-2.29.so
7fe2a633b000-7fe2a633e000 rw-p 001e3000 08:11 3678270                    /usr/lib/x86_64-linux-gnu/libc-2.29.so
7fe2a633e000-7fe2a6344000 rw-p 00000000 00:00 0 
7fe2a6347000-7fe2a6349000 r--p 00000000 08:11 3811878                    /usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
7fe2a6349000-7fe2a634b000 r-xp 00002000 08:11 3811878                    /usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
7fe2a634b000-7fe2a634c000 r--p 00004000 08:11 3811878                    /usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
7fe2a634c000-7fe2a634d000 r--p 00004000 08:11 3811878                    /usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
7fe2a634d000-7fe2a634e000 rw-p 00005000 08:11 3811878                    /usr/lib/python3.7/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
7fe2a634e000-7fe2a6351000 r--p 00000000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6351000-7fe2a6354000 r-xp 00003000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6354000-7fe2a6355000 r--p 00006000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6355000-7fe2a6356000 ---p 00007000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6356000-7fe2a6357000 r--p 00007000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6357000-7fe2a6359000 rw-p 00008000 08:11 3811912                    /usr/lib/python3.7/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
7fe2a6359000-7fe2a6360000 r--s 00000000 08:11 4328730                    /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
7fe2a6360000-7fe2a6361000 r--p 00000000 08:11 3678050                    /usr/lib/x86_64-linux-gnu/ld-2.29.so
7fe2a6361000-7fe2a6382000 r-xp 00001000 08:11 3678050                    /usr/lib/x86_64-linux-gnu/ld-2.29.so
7fe2a6382000-7fe2a638a000 r--p 00022000 08:11 3678050                    /usr/lib/x86_64-linux-gnu/ld-2.29.so
7fe2a638a000-7fe2a638b000 r--p 00029000 08:11 3678050                    /usr/lib/x86_64-linux-gnu/ld-2.29.so
7fe2a638b000-7fe2a638c000 rw-p 0002a000 08:11 3678050                    /usr/lib/x86_64-linux-gnu/ld-2.29.so
7fe2a638c000-7fe2a638d000 rw-p 00000000 00:00 0 
7fff37dcf000-7fff37df0000 rw-p 00000000 00:00 0                          [stack]
7fff37df1000-7fff37df4000 r--p 00000000 00:00 0                          [vvar]
7fff37df4000-7fff37df5000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
</pre>
</details>
<p>011ac000-01487000 - heap</p>
<p>7fff37dcf000-7fff37df0000 - stack</p>
<p>7fe2a3d7f000-7fe2a3d83000 - Memory Mapping Segment</p>
<p>I hope i undestand idea of memory managment, but without true task not sure... yet.</p>
<p></p>
<h2>Task 6. ## TCP. UDP. Network - #done</h2>
<p><img src="/task_networks/internet101_done.png" alt="task6_done"/></p>
<p><img src="/task_networks/networking_for_web_developers.png" alt="task6_done"/></p>
