#!/usr/bin/env ruby
# match cases of repeated 'b or o'
puts ARGV[0].scan(/hbo?[t]*n$/).join
