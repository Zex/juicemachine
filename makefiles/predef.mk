# makefiles/predef.mk

CC		= gcc
CXX		= g++
TOUCH	= touch
MKDIR	= mkdir -p
RM		= rm -rf
LN		= ln -sf
ECHO	= echo

ifndef PROJECT
$(error PROJECT not defined)
endif

PROJECT_ALIAS	= $(shell echo $(PROJECT)|tr '[:upper:]' '[:lower:]')
PROJECT_DIR		= $(shell pwd)
BUILD			= $(PROJECT_DIR)/build
VERSION_HEADER	= $(BUILD)/version.h

PBVERSION		= 3.0.0
PROTO_BASE		= $(PROJECT_DIR)/proto
PROTOC			= $(PROJECT_DIR)/tools/protobuf-$(PLATFORM)-$(PBVERSION)/protoc

SOURCES			= $(shell find $(SRCS) -iregex ".*\.c\(c\|pp\|++\|xx\)")

CFLAGS			+= -Wall -Wno-pmf-conversions -O0 -g --std=c++11 -fPIC -Wl,--hash-style=sysv -MP -MMD #-fstats#--verbose
LDFLAGS			+=
MACROS			+=
LIBS			+= pthread rt

SHARED_OBJ		= $(BUILD)/lib$(PROJECT_ALIAS).so
OBJS			= $(patsubst %.cpp, $(BUILD)/%.o, $(SOURCES))

ifeq ($(SCM),svn)
	REVISION		= $(shell svn info|grep "Last Changed Rev"|cut -f2 -d:|cut -f2 -d\ )
else ifeq ($(SCM),git)
	REVISION		= $(shell git log |head -1|cut -f2 -d\ |sed -r 's/(.{5})/\1-/g'|cut -f-8 -d-)
else
	REVISION		= None
endif
