MODULES := lib/hooks lib/lexers

LUA_BASE_SRC += \
	lib/base64.lua \
	lib/bit.lua \
	lib/cookie.lua \
	lib/counters.lua \
	lib/DataDumper.lua \
	lib/date.lua \
	lib/defence.lua \
	lib/diag.lua \
	lib/dkjson.lua \
	lib/extensions.lua \
	lib/globtopattern.lua \
	lib/hkdf.lua \
	lib/hmac.lua \
	lib/hooks.lua \
	lib/idn.lua \
	lib/immunio-schemas/immunio_schemas/schemas/request_schema.lua \
	lib/immunio-schemas/immunio_schemas/schemas/validation.lua \
	lib/ip.lua \
	lib/learn.lua \
	lib/lexgraph.lua \
	lib/lexer.lua \
	lib/lru.lua \
	lib/neturl.lua \
	lib/pathname.lua \
	lib/perf.lua \
	lib/permit.lua \
	lib/profiler.lua \
	lib/real_ip.lua \
	lib/sanitize_sql.lua \
	lib/sanitize_command.lua \
	lib/semver.lua \
	lib/sha1.lua \
	lib/snap.lua \
	lib/term.lua \
	lib/tracking.lua \
	lib/utils.lua \
	lib/verb_tamper.lua

include $(patsubst %, %/module.mk,$(MODULES))
