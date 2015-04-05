# Makefile for cpp source
#
# Author: Zex <top_zlynch@yahoo.com>
#

PROJECT	 := jm_object
PLATFORM := intel_linux
OUT_BASE := $(BUILD)/src
CXXFLAGS := `pkg-config --cflags --libs python3`

include ../makefiles/predef.mk

jm_object: jm_object.cpp
	$(MKDIR) $(OUT_BASE)
	$(CXX) $(CXXFLAGS) $^ -o $(OUT_BASE)/$@
