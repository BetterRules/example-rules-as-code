# frozen_string_literal: true
require './beard_checker'

class FacialHair
  def length_in_mm
    @length
  end

  def on_or_below_chin
    false
  end

  def unbroken_between_ears
    false
  end

  def is_beard?
    BeardChecker.is_beard?(
      length_in_mm: length_in_mm,
      on_or_below_chin: on_or_below_chin,
      unbroken_between_ears: unbroken_between_ears
    )
  end
end

class MuttonChops < FacialHair
  def initialize(length:, friendly: false)
    @length = length
    @friendly = friendly
  end

  def on_or_below_chin
    false
  end

  def unbroken_between_ears
    @friendly ? true : false
  end
end

class Goatee < FacialHair
  def initialize(length:)
    @length = length
  end

  def on_or_below_chin
    true
  end

  def unbroken_between_ears
    false
  end
end

class Moustache < FacialHair
  def initialize(length:)
    @length = length
  end

  def on_or_below_chin
    false
  end

  def unbroken_between_ears
    false
  end
end

class HairyMole < FacialHair
  def initialize(length:, location: :cheek)
    @length = length
    @location = location
  end

  def on_or_below_chin
    return true if location == :chin
    return true if location == :jaw
    return true if location == :throat

    false
  end

  def unbroken_between_ears
    false
  end
end

class FullBeard < FacialHair
  def initialize(length:, density: 0.7)
    @length = length
    @density = density
  end

  def on_or_below_chin
    true
  end

  def unbroken_between_ears
    true
  end

  def is_impressive?
    @length >= 20 && @density >= 0.9
  end
end
