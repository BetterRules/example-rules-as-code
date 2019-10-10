#!/usr/bin/env python


class Person(object):
    def has_a_beard(self):
        return self.facial_hair_length_gt_5 and (
            self.facial_hair_on_chin or self.facial_hair_uninterupted)


if __name__ == "__main__":
    f = Person()
    f.facial_hair_length_gt_5 = True
    f.facial_hair_on_chin = True

    print("Has a beard", f.has_a_beard())
