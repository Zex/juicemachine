# Proto Makefile

PROJECT		:= JuiceMachine
PLATFORM	:= intel_linux

include ../makefiles/predef.mk

CPP_OUT	:= $(BUILD)/$(COMP)_cpp
PY_OUT	:= $(BUILD)/$(COMP)_py

all: $(COMP)

$(COMP):
	$(ECHO) "Generating interfaces for component $(COMP)"
	$(MKDIR) $(CPP_OUT) $(PY_OUT)
	$(PROTOC) --cpp_out=$(CPP_OUT) --python_out=$(PY_OUT) $(PROTO_BASE)/$(COMP).proto


