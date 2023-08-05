// Gmsh project created on Sun Jun 11 18:02:16 2017
SetFactory("OpenCASCADE");
DefineConstant[
N = {20, Name "Input/1Points "},
// L = {1,  Name "Input/2Rect "},
r =  {1, Name "Input/2Radius"},
R1 = {15, Name "Input/3Big Radius"},
R2 = {5, Name "Input/4Upper length"}
];

N=(N>=1 ? N : 1);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = (R1+R2+r)/(N+10);
Mesh.CharacteristicLengthMax = (R1+R2+r)/(N+10);

//+
Sphere(1) = {0, 0, 0, R2, -Pi/2, Pi/2, 2*Pi};
Sphere(2) = {R1, 0, 0, R2, -Pi/2, Pi/2, 2*Pi};
Sphere(3) = {-R1, 0, 0, R2, -Pi/2, Pi/2, 2*Pi};
Sphere(4) = {0,R1, 0, R2, -Pi/2, Pi/2, 2*Pi};
Sphere(5) = {0,-R1, 0, R2, -Pi/2, Pi/2, 2*Pi};

//+
Torus(10) = {0, 0, 0, R1, r, 2*Pi};
//+
Cylinder(11) = {-R1, 0, 0, 2*R1, 0, 0, r, 2*Pi};
//+
Cylinder(12) = {0, -R1, 0, 0, 2*R1, 0, r, 2*Pi};

BooleanUnion(20) = { Volume{10}; Delete; }{ Volume{2,3,4,5}; Delete; };
BooleanUnion(21) = { Volume{1}; Delete; }{ Volume{11,12}; Delete; };

BooleanUnion(22) = { Volume{20}; Delete; }{ Volume{21}; Delete; };//+

Physical Surface(1) = {8};
//+
Physical Surface(2) = {3, 2, 9, 10};
//+
Physical Surface(3) = {1, 6, 13, 5};
//+
Physical Surface(4) = {11, 12, 4, 7};
//+
Physical Volume(1) = {22};
