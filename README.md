# Update Curve Coordinates v1.0

Transforms a Curve SOP curve and writes the coordinates back to its 'coords' parameter.
The original curve, if stached, is available on Output 1.

It requires a Curve SOP as input! Currently 'onInputChanged' will not warn if other node type is wired as input. WIP.
