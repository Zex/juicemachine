# Top-level Makefile
#
# Author: Zex <top_zlynch@yahoo.com>
#

PROJECT	:= JuiceMachine

include makefiles/predef.mk

all: juicemachine

juicemachine: gen_src

gen_src:
	./scripts/prot2src juicemachine proto build

clean:
	$(RM) build
