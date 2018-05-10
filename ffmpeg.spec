Name:	ffmpeg	
Version: 4.0	
Release:	1%{?dist}
Summary:  ffmpeg  	

Group:	Applications/System
License: LGPL
URL:	http://ffmpeg.org	
Source: ffmpeg-%{version}.tar.gz

Requires:	bash openssl-devel openssl  

%description
My ffmpeg RPM BUILD


%prep
%setup -n ffmpeg-%{version}


%build
./configure --enable-libmp3lame --enable-openssl --enable-gpl --enable-nonfree --enable-libx264 --extra-cflags=-I/usr/local/include --extra-ldflags=-L/usr/local/lib
make %{?_smp_mflags}


%install
%make_install


%files
%doc
   /usr/local/bin/ffmpeg
   /usr/local/bin/ffprobe
   /usr/local/include/libavcodec/ac3_parser.h
   /usr/local/include/libavcodec/adts_parser.h
   /usr/local/include/libavcodec/avcodec.h
   /usr/local/include/libavcodec/avdct.h
   /usr/local/include/libavcodec/avfft.h
   /usr/local/include/libavcodec/d3d11va.h
   /usr/local/include/libavcodec/dirac.h
   /usr/local/include/libavcodec/dv_profile.h
   /usr/local/include/libavcodec/dxva2.h
   /usr/local/include/libavcodec/jni.h
   /usr/local/include/libavcodec/mediacodec.h
   /usr/local/include/libavcodec/qsv.h
   /usr/local/include/libavcodec/vaapi.h
   /usr/local/include/libavcodec/vdpau.h
   /usr/local/include/libavcodec/version.h
   /usr/local/include/libavcodec/videotoolbox.h
   /usr/local/include/libavcodec/vorbis_parser.h
   /usr/local/include/libavcodec/xvmc.h
   /usr/local/include/libavdevice/avdevice.h
   /usr/local/include/libavdevice/version.h
   /usr/local/include/libavfilter/avfilter.h
   /usr/local/include/libavfilter/buffersink.h
   /usr/local/include/libavfilter/buffersrc.h
   /usr/local/include/libavfilter/version.h
   /usr/local/include/libavformat/avformat.h
   /usr/local/include/libavformat/avio.h
   /usr/local/include/libavformat/version.h
   /usr/local/include/libavutil/adler32.h
   /usr/local/include/libavutil/aes.h
   /usr/local/include/libavutil/aes_ctr.h
   /usr/local/include/libavutil/attributes.h
   /usr/local/include/libavutil/audio_fifo.h
   /usr/local/include/libavutil/avassert.h
   /usr/local/include/libavutil/avconfig.h
   /usr/local/include/libavutil/avstring.h
   /usr/local/include/libavutil/avutil.h
   /usr/local/include/libavutil/base64.h
   /usr/local/include/libavutil/blowfish.h
   /usr/local/include/libavutil/bprint.h
   /usr/local/include/libavutil/bswap.h
   /usr/local/include/libavutil/buffer.h
   /usr/local/include/libavutil/camellia.h
   /usr/local/include/libavutil/cast5.h
   /usr/local/include/libavutil/channel_layout.h
   /usr/local/include/libavutil/common.h
   /usr/local/include/libavutil/cpu.h
   /usr/local/include/libavutil/crc.h
   /usr/local/include/libavutil/des.h
   /usr/local/include/libavutil/dict.h
   /usr/local/include/libavutil/display.h
   /usr/local/include/libavutil/downmix_info.h
   /usr/local/include/libavutil/encryption_info.h
   /usr/local/include/libavutil/error.h
   /usr/local/include/libavutil/eval.h
   /usr/local/include/libavutil/ffversion.h
   /usr/local/include/libavutil/fifo.h
   /usr/local/include/libavutil/file.h
   /usr/local/include/libavutil/frame.h
   /usr/local/include/libavutil/hash.h
   /usr/local/include/libavutil/hmac.h
   /usr/local/include/libavutil/hwcontext.h
   /usr/local/include/libavutil/hwcontext_cuda.h
   /usr/local/include/libavutil/hwcontext_d3d11va.h
   /usr/local/include/libavutil/hwcontext_drm.h
   /usr/local/include/libavutil/hwcontext_dxva2.h
   /usr/local/include/libavutil/hwcontext_mediacodec.h
   /usr/local/include/libavutil/hwcontext_qsv.h
   /usr/local/include/libavutil/hwcontext_vaapi.h
   /usr/local/include/libavutil/hwcontext_vdpau.h
   /usr/local/include/libavutil/hwcontext_videotoolbox.h
   /usr/local/include/libavutil/imgutils.h
   /usr/local/include/libavutil/intfloat.h
   /usr/local/include/libavutil/intreadwrite.h
   /usr/local/include/libavutil/lfg.h
   /usr/local/include/libavutil/log.h
   /usr/local/include/libavutil/lzo.h
   /usr/local/include/libavutil/macros.h
   /usr/local/include/libavutil/mastering_display_metadata.h
   /usr/local/include/libavutil/mathematics.h
   /usr/local/include/libavutil/md5.h
   /usr/local/include/libavutil/mem.h
   /usr/local/include/libavutil/motion_vector.h
   /usr/local/include/libavutil/murmur3.h
   /usr/local/include/libavutil/opt.h
   /usr/local/include/libavutil/parseutils.h
   /usr/local/include/libavutil/pixdesc.h
   /usr/local/include/libavutil/pixelutils.h
   /usr/local/include/libavutil/pixfmt.h
   /usr/local/include/libavutil/random_seed.h
   /usr/local/include/libavutil/rational.h
   /usr/local/include/libavutil/rc4.h
   /usr/local/include/libavutil/replaygain.h
   /usr/local/include/libavutil/ripemd.h
   /usr/local/include/libavutil/samplefmt.h
   /usr/local/include/libavutil/sha.h
   /usr/local/include/libavutil/sha512.h
   /usr/local/include/libavutil/spherical.h
   /usr/local/include/libavutil/stereo3d.h
   /usr/local/include/libavutil/tea.h
   /usr/local/include/libavutil/threadmessage.h
   /usr/local/include/libavutil/time.h
   /usr/local/include/libavutil/timecode.h
   /usr/local/include/libavutil/timestamp.h
   /usr/local/include/libavutil/tree.h
   /usr/local/include/libavutil/twofish.h
   /usr/local/include/libavutil/version.h
   /usr/local/include/libavutil/xtea.h
   /usr/local/include/libpostproc/postprocess.h
   /usr/local/include/libpostproc/version.h
   /usr/local/include/libswresample/swresample.h
   /usr/local/include/libswresample/version.h
   /usr/local/include/libswscale/swscale.h
   /usr/local/include/libswscale/version.h
   /usr/local/lib/libavcodec.a
   /usr/local/lib/libavdevice.a
   /usr/local/lib/libavfilter.a
   /usr/local/lib/libavformat.a
   /usr/local/lib/libavutil.a
   /usr/local/lib/libpostproc.a
   /usr/local/lib/libswresample.a
   /usr/local/lib/libswscale.a
   /usr/local/lib/pkgconfig/libavcodec.pc
   /usr/local/lib/pkgconfig/libavdevice.pc
   /usr/local/lib/pkgconfig/libavfilter.pc
   /usr/local/lib/pkgconfig/libavformat.pc
   /usr/local/lib/pkgconfig/libavutil.pc
   /usr/local/lib/pkgconfig/libpostproc.pc
   /usr/local/lib/pkgconfig/libswresample.pc
   /usr/local/lib/pkgconfig/libswscale.pc
   /usr/local/share/ffmpeg/examples/Makefile
   /usr/local/share/ffmpeg/examples/README
   /usr/local/share/ffmpeg/examples/avio_dir_cmd.c
   /usr/local/share/ffmpeg/examples/avio_reading.c
   /usr/local/share/ffmpeg/examples/decode_audio.c
   /usr/local/share/ffmpeg/examples/decode_video.c
   /usr/local/share/ffmpeg/examples/demuxing_decoding.c
   /usr/local/share/ffmpeg/examples/encode_audio.c
   /usr/local/share/ffmpeg/examples/encode_video.c
   /usr/local/share/ffmpeg/examples/extract_mvs.c
   /usr/local/share/ffmpeg/examples/filter_audio.c
   /usr/local/share/ffmpeg/examples/filtering_audio.c
   /usr/local/share/ffmpeg/examples/filtering_video.c
   /usr/local/share/ffmpeg/examples/http_multiclient.c
   /usr/local/share/ffmpeg/examples/hw_decode.c
   /usr/local/share/ffmpeg/examples/metadata.c
   /usr/local/share/ffmpeg/examples/muxing.c
   /usr/local/share/ffmpeg/examples/qsvdec.c
   /usr/local/share/ffmpeg/examples/remuxing.c
   /usr/local/share/ffmpeg/examples/resampling_audio.c
   /usr/local/share/ffmpeg/examples/scaling_video.c
   /usr/local/share/ffmpeg/examples/transcode_aac.c
   /usr/local/share/ffmpeg/examples/transcoding.c
   /usr/local/share/ffmpeg/examples/vaapi_encode.c
   /usr/local/share/ffmpeg/examples/vaapi_transcode.c
   /usr/local/share/ffmpeg/ffprobe.xsd
   /usr/local/share/ffmpeg/libvpx-1080p.ffpreset
   /usr/local/share/ffmpeg/libvpx-1080p50_60.ffpreset
   /usr/local/share/ffmpeg/libvpx-360p.ffpreset
   /usr/local/share/ffmpeg/libvpx-720p.ffpreset
   /usr/local/share/ffmpeg/libvpx-720p50_60.ffpreset
   /usr/local/share/man/man1/ffmpeg-all.1
   /usr/local/share/man/man1/ffmpeg-bitstream-filters.1
   /usr/local/share/man/man1/ffmpeg-codecs.1
   /usr/local/share/man/man1/ffmpeg-devices.1
   /usr/local/share/man/man1/ffmpeg-filters.1
   /usr/local/share/man/man1/ffmpeg-formats.1
   /usr/local/share/man/man1/ffmpeg-protocols.1
   /usr/local/share/man/man1/ffmpeg-resampler.1
   /usr/local/share/man/man1/ffmpeg-scaler.1
   /usr/local/share/man/man1/ffmpeg-utils.1
   /usr/local/share/man/man1/ffmpeg.1
   /usr/local/share/man/man1/ffprobe-all.1
   /usr/local/share/man/man1/ffprobe.1
   /usr/local/share/man/man3/libavcodec.3
   /usr/local/share/man/man3/libavdevice.3
   /usr/local/share/man/man3/libavfilter.3
   /usr/local/share/man/man3/libavformat.3
   /usr/local/share/man/man3/libavutil.3
   /usr/local/share/man/man3/libswresample.3
   /usr/local/share/man/man3/libswscale.3




%changelog

