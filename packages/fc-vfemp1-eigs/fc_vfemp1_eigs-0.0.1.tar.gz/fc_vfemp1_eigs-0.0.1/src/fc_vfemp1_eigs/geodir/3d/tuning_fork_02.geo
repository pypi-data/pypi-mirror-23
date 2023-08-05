// Gmsh project created on Thu Jun  1 11:18:57 2017

SetFactory("OpenCASCADE");

DefineConstant[
N = {20, Name "Input/1Points "},
// L = {1,  Name "Input/2Rect "},
r = {10, Name "Input/2Radius"},
R = {40, Name "Input/3Big Radius"},
L = {120, Name "Input/4Upper length"},
l = {80, Name "Input/5Lower length"}
];

N=(N>=1 ? N : 1);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = (L+l+R+r)/(N+10);
Mesh.CharacteristicLengthMax = (L+l+R+r)/(N+10);

Torus(1) = {0, -0, 0, R, r, Pi};

Cylinder(2) = {0, R, 0, 0, l, 0, r, 2*Pi};

Cylinder(3) = {-R, -L, 0, 0, L, 0, r, 2*Pi};

Cylinder(4) = {R, -L, 0, 0, L, 0, r, 2*Pi};

BooleanUnion(10) = { Volume{1}; Delete; }{ Volume{2,3,4}; Delete; };

Rotate {{1, 0, 0}, {0, 0, 0}, -Pi/2} {
   Volume{10};  
 }
 
Physical Surface(1) = {1};
Physical Surface(2) = {2};
Physical Surface(3) = { 3, 5, 4, 7, 6};
Surface Loop(2) = {2, 1, 3, 4, 6, 5, 7};
Physical Volume(1) = {10};
 
