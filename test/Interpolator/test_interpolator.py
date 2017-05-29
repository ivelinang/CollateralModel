from unittest import TestCase

__author__ = 'Ivelin'


class TestInterpolator(TestCase):

  def test_interpolate_f(self):
    from main.Interpolator.Interpolator import Interpolator
    x_axis=[1,2,3,4]
    y_axis=[10,20,30,40]
    keypoint=2.62
    order=1
    result = Interpolator.interpolate1d(x_axis, y_axis, keypoint, order)
    expected_result=0.38*20+0.62*30
    self.assertTrue(abs(result-expected_result)<10**-6)


  def test_interpolate1d(self):
    self.assertTrue(1==1)
