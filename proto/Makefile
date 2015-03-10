# Proto Makefile

PROJECT		:= JuiceMachine
PLATFORM	:= intel_linux

include ../makefiles/predef.mk

CPP_OUT	:= $(BUILD)/$(COMP)_cpp
PY_OUT	:= $(BUILD)/$(COMP)_py

PROTOC_FLAGS = --proto_path=$(PROTO_BASE)

export LD_LIBRARY_PATH=$(PROTOBUF_BASE)

ifdef CPP_OUT
PROTOC_FLAGS += --cpp_out=$(CPP_OUT)
endif

ifdef PY_OUT
PROTOC_FLAGS += --python_out=$(PY_OUT)
endif

all: $(COMP)

$(COMP):
	$(ECHO) "Generating interfaces for component $(COMP)"
	$(MKDIR) $(CPP_OUT) $(PY_OUT)
	$(PROTOC) $(PROTOC_FLAGS) $(PROTO_BASE)/$(COMP).proto

clean:
	$(RM) $(CPP_OUT) $(PY_OUT)

