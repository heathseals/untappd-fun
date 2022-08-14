#!/usr/bin/env ruby
# frozen_string_literal: true

require 'json'

if ARGV.length != 1
  puts 'One and only one argument please.'
  exit
end

puts "Working on #{ARGV}"

file = File.read(ARGV.first)
data = JSON.parse(file)

(2010..Time.now.year).each do |year|
  current_year = data.map { |x| x['beer_abv'].to_f if x['created_at'].include? year.to_s }.compact
  current_year.delete(0)
  next if current_year.size.zero?

  avg_abv = current_year.inject { |sum, el| sum + el } / current_year.size
  puts "#{year} : #{current_year.min}% min | #{avg_abv.round(2)}% avg | #{current_year.max}% max \
  | #{current_year.size} unique check-ins."
end

all_years = data.map { |x| x['beer_abv'].to_f }.compact
all_years.delete(0)
avg_abv = all_years.inject { |sum, el| sum + el } / all_years.size
puts "All  : #{all_years.min}% min | #{avg_abv.round(2)}% avg | #{all_years.max}% max | \
#{all_years.size} unique check-ins."
