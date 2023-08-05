DefineConstant[
N = {20, Name "Input/1Points "}
// L = {1,  Name "Input/2Rect "},
// r = {0.1, Name "Input/3Radius"}
];

N=(N>=10 ? N : 10);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = 100/N;
Mesh.CharacteristicLengthMax = 100/N;


Merge "TuningFork440Hz.STEP";


Physical Surface(1) = {51};
//+
Physical Surface(2) = {50, 1, 20, 2, 19, 24, 4, 35, 18, 3, 49, 31, 11, 42, 29, 12, 43, 41, 10, 33, 36, 40, 5, 9, 44, 48, 26, 34, 13, 17, 27, 21, 37, 38, 39, 6, 7, 8, 45, 28, 46, 30, 47, 32, 14, 15, 16, 25, 23, 22};
//+
Physical Volume(3) = {1};
