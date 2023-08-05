#!/usr/bin/env ruby
# match 10 digits in an argument
puts ARGV[0].scan(/^[0-9]{10}/).join
