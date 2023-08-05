#!/usr/bin/env ruby
#  match all cases of hb[t]+/n
puts ARGV[0].scan(/hb[t]*n$/).join
