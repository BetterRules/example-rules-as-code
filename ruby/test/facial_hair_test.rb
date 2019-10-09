# frozen_string_literal: true

require 'minitest/autorun'
require './facial_hair'

class TestFacialHair < Minitest::Test
  def test_friendly_mutton_chops
    beard = MuttonChops.new(length: 10, friendly: true)
    assert beard.is_beard?
  end
  def test_unfriendly_mutton_chops
    beard = MuttonChops.new(length: 10, friendly: false)
    refute beard.is_beard?
  end
  def test_goatee
    beard = Goatee.new(length: 10)
    assert beard.is_beard?
  end
  def test_bumfluff
    beard = Goatee.new(length: 2)
    refute beard.is_beard?
  end
  def test_moustache
    beard = Moustache.new(length: 30)
    refute beard.is_beard?
  end
  def test_full_beard
    beard = FullBeard.new(length: 50, density: 0.9)
    assert beard.is_beard?
    assert beard.is_impressive?
  end
end
