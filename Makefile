# Top-level Makefile
#
# Author: Zex <top_zlynch@yahoo.com>
#

PROJECT		:= JuiceMachine
PLATFORM	:= intel_linux

include makefiles/predef.mk

all: juicemachine

juicemachine:
	$(MAKE) PROJECT_DIR=$(PROJECT_DIR) BUILD=$(BUILD) COMP=$@ -C proto $@ 

#gen_src:
#./scripts/prot2src juicemachine proto build

clean:
	$(RM) build

jm_object:
	$(MAKE) PROJECT_DIR=$(PROJECT_DIR) BUILD=$(BUILD) -C src/ $@


htmldoc:
	doxygen Doxyfile
