protobuf:
	pushd protobuf-3.0.0-alpha-1;\
	unzip gtest-1.7.0.zip;\
	mv gtest-1.7.0 gtest;\
	./autogen.sh;\
	./configure --prefix=/home/zex/lab/juicemachine/extern;\
	make;\
	make install;\
	popd

protobuf-c:
	pushd protobuf-c;\
	./autogen.sh;\
	./configure --prefix=/home/zex/lab/juicemachine/extern\
		protobuf_LIBS="-L/home/zex/lab/juicemachine/extern/lib/ -lprotobuf -lpthread"\
		protobuf_CFLAGS="-I/home/zex/lab/juicemachine/extern/include/"\
		PROTOC=/home/zex/lab/juicemachine/extern/bin/protoc;\
	make;\
	make install;\
	popd
