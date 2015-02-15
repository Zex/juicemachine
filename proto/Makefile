# Proto Makefile

PROJECT		:= JuiceMachine
PLATFORM	:= intel_linux

include ../makefiles/predef.mk

CPP_OUT	:= $(BUILD)/$(COMP)_cpp
PY_OUT	:= $(BUILD)/$(COMP)_py

export LD_LIBRARY_PATH=$(PROTOBUF_BASE)

all: $(COMP)

$(COMP):
	$(ECHO) "Generating interfaces for component $(COMP)"
	$(MKDIR) $(CPP_OUT) $(PY_OUT)
	$(PROTOC) --cpp_out=$(CPP_OUT) --python_out=$(PY_OUT) --proto_path=$(PROTO_BASE) $(PROTO_BASE)/$(COMP).proto



