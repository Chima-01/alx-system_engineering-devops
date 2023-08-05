#!/usr/bin/env ruby
# match word that starts with h and end with n
puts ARGV[0].scan(/^h[\w]+n$/).join
