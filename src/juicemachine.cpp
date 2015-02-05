#include "build/juicemachine_cpp/proto/juicemachine.pb.h"

int main(int argc, char* argv[])
{
    Juice juice;

    juice.set_id(1234567);
    juice.set_data_len(128);

    return 0;
}
