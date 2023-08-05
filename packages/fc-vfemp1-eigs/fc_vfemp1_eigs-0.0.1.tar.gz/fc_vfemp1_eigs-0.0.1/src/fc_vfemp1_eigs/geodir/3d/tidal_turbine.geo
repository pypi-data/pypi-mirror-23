DefineConstant[
N = {4, Name "Input/1Points "}
];

N=(N>=4 ? N : 4);

Merge "tidal_turbine.STEP";

//Mesh.Algorithm3D=4; // for Netgen
Mesh.CharacteristicLengthMin = 2/N;
Mesh.CharacteristicLengthMax = 10/N;

Physical Surface(1) = {63, 79, 5, 88, 80, 4, 38, 30, 81, 2, 84, 87, 6, 78, 7, 77, 3, 82, 1, 83};
//+
Physical Surface(2) = { 20, 19, 10, 44, 11, 45, 73, 74, 21, 43, 18, 9, 12, 46, 72, 75, 48, 51, 49, 50, 53, 39, 52, 56, 54, 55, 69, 68, 29, 86, 13, 22, 58, 61, 59, 60, 71, 64, 27, 62, 42, 24, 66, 57, 67, 65, 25, 85, 33, 36, 37, 31, 32, 35, 34};
//+
Physical Volume(1) = {1};
