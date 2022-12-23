#!/home/wandb/.rvm/rubies/ruby-2.7.5/bin/ruby
require 'cgi'
require 'uri'

TARGET = 'https://uv-v4.netlify.app/#?manifest='
#TARGET = 'https://www.wallandbinkley.com/'

cgi = CGI.new

# find first line beginning with "IIIF:" and extract manifest uri

blob = cgi.params['zotero-extra'].first
lines = blob.to_s.split("\n").map { |line| line = line.strip }
line = lines.select { |line| line.start_with?('IIIF:')}.first
manifest = URI.regexp.match(line.sub(/^IIIF:/, '').strip)
redirect = TARGET + CGI.escape(manifest.to_s)

cgi.out('status' => '302', 'location' => redirect) {'redirected'}

=begin
x = "Params:\n"
cgi.params.keys.each { |key| x += "#{key}: #{cgi.params[key]}\n"}
cgi.out('status' => '200') { x }
=end