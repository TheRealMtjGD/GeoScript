Value declorations
==========================

Allocate variable
--------------------------
###### static
id: 1817
adress: 80
value: 77

1,1817,2,135,3,135,155,1,36,1,80,3420,77,69420,139,1,449,1

###### dynamic
id: 3619
adress: 80
adress2: 51

1,3619,2,195,3,135,155,1,36,1,80,69420,476,1,478,1,51,3420,479,1,481,1,482,3

Modify variable
--------------------------
###### static
id: 1817
adress: 80
value: 77

special operations
{
    multiply: 88,1
    divide: 88,2
}

1,1817,2,165,3,105,155,1,36,1,80,3420,77,69420,449,69420

###### dynamic
id: 3619
adress: 80
adress2: 51

special operations (add 481,1)
{
    add: 480,1
    subtract: 480,2
    multiply: 480,3
    divide: 480,4
}

1,3619,2,195,3,135,155,1,36,1,80,69420,476,1,478,1,51,3420,479,1,481,1,482,3

Controll flow
===================
###### static
id: 3620
adress1: 80
adress2: 483
tid: 51
fid: 71

{
    > : 482,1
    >= : 482,2
    < : 482,3
    <= : 482,4
    != : 482,5
}

1,3620,2,165,3,105,155,1,36,1,80,69,51,469,71,694,476,1,479,1,483,420,480,3,481,3

###### dynamic
id: 3620
adress1: 80
adress2: 95
tid: 51
fid: 71

{
    > : 482,1
    >= : 482,2
    < : 482,3
    <= : 482,4
    != : 482,5
}

1,3620,2,165,3,105,155,1,36,1,80,69,95,420,51,469,71,694,476,1,477,1,479,1,483,1,480,3,481,3

Objects
==============

Spawn trigger
---------------
id: 1268
group: 51

1,1268,2,165,3,105,155,1,36,1,51,420

Sequence trigger
---------------
id: 3607
delay: 437
loop-mode: 436,1
jmp-scope: 435

1,3607,2,165,3,105,155,1,87,1,36,1,437,69420,435,69.1.420.2

ETC
=======
spawn_trigger: 62,1
multi_trigger: 87,1