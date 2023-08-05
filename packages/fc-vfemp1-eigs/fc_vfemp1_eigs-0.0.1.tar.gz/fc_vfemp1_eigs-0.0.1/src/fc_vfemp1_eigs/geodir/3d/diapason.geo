// Gmsh project created on Thu Jun  1 11:18:57 2017

SetFactory("OpenCASCADE");

DefineConstant[
N = {20, Name "Input/1Points "}
// L = {1,  Name "Input/2Rect "},
// r = {0.1, Name "Input/3Radius"}
];

N=(N>=10 ? N : 10);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = 10/N;
Mesh.CharacteristicLengthMax = 10/N;

Torus(1) = {0, -0, 0, 4, 1, Pi};

//+
Cylinder(2) = {0, 4, 0, 0, 16, 0, 1, 2*Pi};

//+

//+
Cylinder(3) = {-4, -10, 0, 0, 10, 0, 1, 2*Pi};
//+
Cylinder(4) = {4, -10, 0, 0, 10, 0, 1, 2*Pi};
//+
BooleanUnion(10) = { Volume{1}; Delete; }{ Volume{2,3,4}; Delete; };
//BooleanUnion(11) = { Volume{10}; Delete; }{ Volume{3,4}; Delete; };

/*

//+
//+*/
//+
// Rotate {{1, 0, 0}, {0, 4, 0}, Pi/2} {
//   Duplicata { Line{1}; Line{2}; Line{3}; Line{4}; Line{5}; Line{6}; Line{9}; Line{8}; Line{7}; Line{13}; Line{14}; Line{16}; Line{15}; Line{11}; Line{12}; Line{10}; }
// }

 Rotate {{1, 0, 0}, {0, 4, 0}, -Pi/2} {
   Volume{10};  
 }
 
 
Physical Surface(1) = {1};
 //+
Physical Surface(2) = {2, 3, 5, 4, 7, 6};
 //+
Surface Loop(2) = {2, 1, 3, 4, 6, 5, 7};
 //+
 //+
Physical Volume(1) = {10};
 
