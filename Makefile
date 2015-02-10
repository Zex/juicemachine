# Top-level Makefile
#
# Author: Zex <top_zlynch@yahoo.com>
#

PROJECT		:= JuiceMachine
PLATFORM	:= intel_linux
PBVERSION	:= 3.0.0
PBTOOLS		:= protobuf-$(PLATFORM)-$(PBVERSION)
PBPATH		:= tools/$(PBTOOLS)/protoc

include makefiles/predef.mk

all: juicemachine

juicemachine: gen_src

gen_src:
	./scripts/prot2src juicemachine proto build

clean:
	$(RM) build

htmldoc:
	doxygen Doxyfile
