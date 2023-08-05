// Gmsh project created on Sun Jun 11 18:02:16 2017
SetFactory("OpenCASCADE");
DefineConstant[
N = {20, Name "Input/1Points "},
// L = {1,  Name "Input/2Rect "},
r =  {1, Name "Input/2r"},
R1 = {15, Name "Input/3R1"},
R2 = {5, Name "Input/4R2"}
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
Sphere(6) = {0,0,R1, R2, -Pi/2, Pi/2, 2*Pi};
Sphere(7) = {0,0,-R1, R2, -Pi/2, Pi/2, 2*Pi};

//+
Torus(10) = {0, 0, 0, R1, r, 2*Pi};
Torus(11) = {0, 0, 0, R1, r, 2*Pi};
Rotate {{0, 1, 0}, {0, 0, 0}, Pi/2} {
   Volume{11}; 
}
Torus(12) = {0, 0, 0, R1, r, 2*Pi};
Rotate {{1, 0, 0}, {0, 0, 0}, Pi/2} {
   Volume{12}; 
}

//+
Cylinder(21) = {-R1, 0, 0, 2*R1, 0, 0, r, 2*Pi};
//+
Cylinder(22) = {0, -R1, 0, 0, 2*R1, 0, r, 2*Pi};
Cylinder(23) = {0, 0 , -R1, 0,  0, 2*R1, r, 2*Pi};
//+
BooleanUnion(30) = { Volume{1,2,3,4,5,6,7}; Delete; }{ Volume{10,11,12,21,22,23}; Delete; };

//BooleanUnion(31) = { Volume{30}; Delete; }{ Volume{10}; Delete; };
//BooleanUnion(32) = { Volume{31}; Delete; }{ Volume{11}; Delete; };
//BooleanUnion(33) = { Volume{32}; Delete; }{ Volume{12}; Delete; };


//+
Physical Surface(1) = {1};
//+
Physical Surface(2) = {9};
//+
Physical Surface(3) = {11};
//+
Physical Surface(4) = {12};
//+
Physical Surface(5) = {13};
//+
Physical Surface(6) = {8};
//+
Physical Surface(7) = {10};
//+
Physical Surface(8) = {7, 6, 5, 3, 2, 4};
//+
Physical Surface(9) = {16, 17, 15, 14, 19, 25, 24, 22, 21, 23, 18, 20};
//+
Physical Volume(10) = {30};
//+
//+
