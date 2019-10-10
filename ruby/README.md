# Ruby beard checker

- bundle install
- bundle exec ruby test/beard_checker_test.rb

This is structured as a service object.

```ruby
require 'beard_checker'

BeardChecker.is_beard?(
    length_in_mm: 5,
    on_or_below_chin: false,
    unbroken_between_ears: false)
```
