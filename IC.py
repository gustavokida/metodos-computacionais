import math
from math import *

def tabelaNormal(significancia):
    tnormal = [0.0000, 0.0040, 0.0080, 0.0120, 0.0160, 0.0199, 0.0239, 0.0279, 0.0319, 0.0359, 0.0398, 0.0438, 0.0478,
               0.0517, 0.0557, 0.0596, 0.0636, 0.0675, 0.0714, 0.0753, 0.0793, 0.0832, 0.0871, 0.0910, 0.0948, 0.0987,
               0.1026, 0.1064, 0.1103, 0.1141, 0.1179, 0.1217, 0.1255, 0.1293, 0.1331, 0.1368, 0.1406, 0.1443, 0.1480,
               0.1517, 0.1554, 0.1591, 0.1628, 0.1664, 0.1700, 0.1736, 0.1772, 0.1808, 0.1844, 0.1879, 0.1915, 0.1950,
               0.1985, 0.2019, 0.2054, 0.2088, 0.2123, 0.2157, 0.2190, 0.2224, 0.2257, 0.2291, 0.2324, 0.2357, 0.2389,
               0.2422, 0.2454, 0.2486, 0.2517, 0.2549, 0.2580, 0.2611, 0.2642, 0.2673, 0.2704, 0.2734, 0.2764, 0.2794,
               0.2823, 0.2852, 0.2881, 0.2910, 0.2939, 0.2967, 0.2995, 0.3023, 0.3051, 0.3078, 0.3106, 0.3133, 0.3159,
               0.3186, 0.3212, 0.3238, 0.3264, 0.3289, 0.3315, 0.3340, 0.3365, 0.3389, 0.3413, 0.3438, 0.3461, 0.3485,
               0.3508, 0.3531, 0.3554, 0.3577, 0.3599, 0.3621, 0.3643, 0.3665, 0.3686, 0.3708, 0.3729, 0.3749, 0.3770,
               0.3790, 0.3810, 0.3830, 0.3849, 0.3869, 0.3888, 0.3907, 0.3925, 0.3944, 0.3962, 0.3980, 0.3997, 0.4015,
               0.4032, 0.4049, 0.4066, 0.4082, 0.4099, 0.4115, 0.4131, 0.4147, 0.4162, 0.4177, 0.4192, 0.4207, 0.4222,
               0.4236, 0.4251, 0.4265, 0.4279, 0.4292, 0.4306, 0.4319, 0.4332, 0.4345, 0.4357, 0.4370, 0.4382, 0.4394,
               0.4406, 0.4418, 0.4429, 0.4441, 0.4452, 0.4463, 0.4474, 0.4484, 0.4495, 0.4505, 0.4515, 0.4525, 0.4535,
               0.4545, 0.4554, 0.4564, 0.4573, 0.4582, 0.4591, 0.4599, 0.4608, 0.4616, 0.4625, 0.4633, 0.4641, 0.4649,
               0.4656, 0.4664, 0.4671, 0.4678, 0.4686, 0.4693, 0.4699, 0.4706, 0.4713, 0.4719, 0.4726, 0.4732, 0.4738,
               0.4744, 0.4750, 0.4756, 0.4761, 0.4767, 0.4772, 0.4778, 0.4783, 0.4788, 0.4793, 0.4798, 0.4803, 0.4808,
               0.4812, 0.4817, 0.4821, 0.4826, 0.4830, 0.4834, 0.4838, 0.4842, 0.4846, 0.4850, 0.4854, 0.4857, 0.4861,
               0.4864, 0.4868, 0.4871, 0.4875, 0.4878, 0.4881, 0.4884, 0.4887, 0.4890, 0.4893, 0.4896, 0.4898, 0.4901,
               0.4904, 0.4906, 0.4909, 0.4911, 0.4913, 0.4916, 0.4918, 0.4920, 0.4922, 0.4925, 0.4927, 0.4929, 0.4931,
               0.4932, 0.4934, 0.4936, 0.4938, 0.4940, 0.4941, 0.4943, 0.4945, 0.4946, 0.4948, 0.4949, 0.4951, 0.4952,
               0.4953, 0.4955, 0.4956, 0.4957, 0.4959, 0.4960, 0.4961, 0.4962, 0.4963, 0.4964, 0.4965, 0.4966, 0.4967,
               0.4968, 0.4969, 0.4970, 0.4971, 0.4972, 0.4973, 0.4974, 0.4974, 0.4975, 0.4976, 0.4977, 0.4977, 0.4978,
               0.4979, 0.4979, 0.4980, 0.4981, 0.4981, 0.4982, 0.4982, 0.4983, 0.4984, 0.4984, 0.4985, 0.4985, 0.4986,
               0.4986, 0.4987, 0.4987, 0.4987, 0.4988, 0.4988, 0.4989, 0.4989, 0.4989, 0.4990, 0.4990, 0.4990, 0.4991,
               0.4991, 0.4991, 0.4992, 0.4992, 0.4992, 0.4992, 0.4993, 0.4993, 0.4993, 0.4993, 0.4994, 0.4994, 0.4994,
               0.4994, 0.4994, 0.4995, 0.4995, 0.4995, 0.4995, 0.4995, 0.4995, 0.4996, 0.4996, 0.4996, 0.4996, 0.4996,
               0.4996, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4997, 0.4998, 0.4998,
               0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4998, 0.4999, 0.4999,
               0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999,
               0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999, 0.4999,
               0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000]

    for i in range(len(tnormal)):
        if significancia == tnormal[i]:
            return float((i)/100)
        elif significancia < tnormal[i]:
            return float((i-1)/100)

def tabelaStudent(confianca, n):
    tstudent = [0.0787, 0.1584, 0.3249, 0.5095, 0.7265, 1.0000, 1.3764, 1.9626, 3.0777, 6.3138, 12.7062, 31.8205,
         63.657, 636.619, 0.0708, 0.1421, 0.2887, 0.4447, 0.6172, 0.8165, 1.0607, 1.3862, 1.8856, 2.9200, 4.3027, 6.9646,
         9.9248, 31.5991, 0.0681, 0.1366, 0.2767, 0.4242, 0.5844, 0.7649, 0.9785, 1.2498, 1.6377, 2.3534, 3.1824, 4.5407,
         5.8409, 12.9240,
         0.0667, 0.1338, 0.2707, 0.4142, 0.5686, 0.7407, 0.9410, 1.1896, 1.5332, 2.1318, 2.7764, 3.7469, 4.6041, 8.6103,
         0.0659, 0.1322, 0.2672, 0.4082, 0.5594, 0.7267, 0.9195, 1.1558, 1.4759, 2.0150, 2.5706, 3.3649, 4.0321, 6.8688,
         0.0654, 0.1311, 0.2648, 0.4043, 0.5534, 0.7176, 0.9057, 1.1342, 1.4398, 1.9432, 2.4469, 3.1427, 3.7074, 5.9588,
         0.0650, 0.1303, 0.2632, 0.4015, 0.5491, 0.7111, 0.8960, 1.1192, 1.4149, 1.8946, 2.3646, 2.9980, 3.4995, 5.4079,
         0.0647, 0.1297, 0.2619, 0.3995, 0.5459, 0.7064, 0.8889, 1.1081, 1.3968, 1.8595, 2.3060, 2.8965, 3.3554, 5.0413,
         0.0645, 0.1293, 0.2610, 0.3979, 0.5435, 0.7027, 0.8834, 1.0997, 1.3830, 1.8331, 2.2622, 2.8214, 3.2498, 4.7809,
         0.0643, 0.1289, 0.2602, 0.3966, 0.5415, 0.6998, 0.8791, 1.0931, 1.3722, 1.8125, 2.2281, 2.7638, 3.1693, 4.5869,
         0.0642, 0.1286, 0.2596, 0.3956, 0.5399, 0.6974, 0.8755, 1.0877, 1.3634, 1.7959, 2.2010, 2.7181, 3.1058, 4.4370,
         0.0640, 0.1283, 0.2590, 0.3947, 0.5386, 0.6955, 0.8726, 1.0832, 1.3562, 1.7823, 2.1788, 2.6810, 3.0545, 4.3178,
         0.0639, 0.1281, 0.2586, 0.3940, 0.5375, 0.6938, 0.8702, 1.0795, 1.3502, 1.7709, 2.1604, 2.6503, 3.0123, 4.2208,
         0.0638, 0.1280, 0.2582, 0.3933, 0.5366, 0.6924, 0.8681, 1.0763, 1.3450, 1.7613, 2.1448, 2.6245, 2.9768, 4.1405,
         0.0638, 0.1278, 0.2579, 0.3928, 0.5357, 0.6912, 0.8662, 1.0735, 1.3406, 1.7531, 2.1314, 2.6025, 2.9467, 4.0728,
         0.0637, 0.1277, 0.2576, 0.3923, 0.5350, 0.6901, 0.8647, 1.0711, 1.3368, 1.7459, 2.1199, 2.5835, 2.9208, 4.0150,
         0.0636, 0.1276, 0.2573, 0.3919, 0.5344, 0.6892, 0.8633, 1.0690, 1.3334, 1.7396, 2.1098, 2.5669, 2.8982, 3.9651,
         0.0636, 0.1274, 0.2571, 0.3915, 0.5338, 0.6884, 0.8620, 1.0672, 1.3304, 1.7341, 2.1009, 2.5524, 2.8784, 3.9216,
         0.0635, 0.1274, 0.2569, 0.3912, 0.5333, 0.6876, 0.8610, 1.0655, 1.3277, 1.7291, 2.0930, 2.5395, 2.8609, 3.8834,
         0.0635, 0.1273, 0.2567, 0.3909, 0.5329, 0.6870, 0.8600, 1.0640, 1.3253, 1.7247, 2.0860, 2.5280, 2.8453, 3.8495,
         0.0635, 0.1272, 0.2566, 0.3906, 0.5325, 0.6864, 0.8591, 1.0627, 1.3232, 1.7207, 2.0796, 2.5176, 2.8314, 3.8193,
         0.0634, 0.1271, 0.2564, 0.3904, 0.5321, 0.6858, 0.8583, 1.0614, 1.3212, 1.7171, 2.0739, 2.5083, 2.8188, 3.7921,
         0.0634, 0.1271, 0.2563, 0.3902, 0.5317, 0.6853, 0.8575, 1.0603, 1.3195, 1.7139, 2.0687, 2.4999, 2.8073, 3.7676,
         0.0634, 0.1270, 0.2562, 0.3900, 0.5314, 0.6848, 0.8569, 1.0593, 1.3178, 1.7109, 2.0639, 2.4922, 2.7969, 3.7454,
         0.0633, 0.1269, 0.2561, 0.3898, 0.5312, 0.6844, 0.8562, 1.0584, 1.3163, 1.7081, 2.0595, 2.4851, 2.7874, 3.7251,
         0.0633, 0.1269, 0.2560, 0.3896, 0.5309, 0.6840, 0.8557, 1.0575, 1.3150, 1.7056, 2.0555, 2.4786, 2.7787, 3.7066,
         0.0633, 0.1268, 0.2559, 0.3894, 0.5306, 0.6837, 0.8551, 1.0567, 1.3137, 1.7033, 2.0518, 2.4727, 2.7707, 3.6896,
         0.0633, 0.1268, 0.2558, 0.3893, 0.5304, 0.6834, 0.8546, 1.0560, 1.3125, 1.7011, 2.0484, 2.4671, 2.7633, 3.6739,
         0.0633, 0.1268, 0.2557, 0.3892, 0.5302, 0.6830, 0.8542, 1.0553, 1.3114, 1.6991, 2.0452, 2.4620, 2.7564, 3.6594,
         0.0632, 0.1267, 0.2556, 0.3890, 0.5300, 0.6828, 0.8538, 1.0547, 1.3104, 1.6973, 2.0423, 2.4573, 2.7500, 3.6460,
         0.0630, 0.1262, 0.2545, 0.3872, 0.5272, 0.6786, 0.8477, 1.0455, 1.2958, 1.6706, 2.0003, 2.3901, 2.6603, 3.4602,
         0.0629, 0.1260, 0.2541, 0.3866, 0.5263, 0.6772, 0.8456, 1.0424, 1.2910, 1.6620, 1.9867, 2.3685, 2.6316, 3.4019,
         0.0628, 0.1259, 0.2539, 0.3862, 0.5258, 0.6765, 0.8446, 1.0409, 1.2886, 1.6577, 1.9799, 2.3578, 2.6174, 3.3735,
         0.0628, 0.1259, 0.2538, 0.3861, 0.5255, 0.6761, 0.8440, 1.0400, 1.2872, 1.6551, 1.9759, 2.3515, 2.6090, 3.3566,
         0.0628, 0.1258, 0.2537, 0.3859, 0.5253, 0.6759, 0.8436, 1.0394, 1.2863, 1.6534, 1.9732, 2.3472, 2.6034, 3.3454,
         0.0628, 0.1258, 0.2537, 0.3858, 0.5252, 0.6757, 0.8433, 1.0390, 1.2856, 1.6521, 1.9713, 2.3442, 2.5994, 3.3375,
         0.0628, 0.1258, 0.2536, 0.3858, 0.5251, 0.6755, 0.8431, 1.0387, 1.2851, 1.6512, 1.9699, 2.3420, 2.5965, 3.3315,
         0.0628, 0.1258, 0.2536, 0.3857, 0.5250, 0.6754, 0.8430, 1.0384, 1.2847, 1.6505, 1.9688, 2.3402, 2.5942, 3.3269,
         0.0628, 0.1258, 0.2536, 0.3857, 0.5250, 0.6753, 0.8428, 1.0382, 1.2844, 1.6499, 1.9679, 2.3388, 2.5923, 3.3233,
         0.0627, 0.1257, 0.2535, 0.3856, 0.5248, 0.6751, 0.8425, 1.0378, 1.2837, 1.6487, 1.9659, 2.3357, 2.5882, 3.3150,
         0.0627, 0.1257, 0.2535, 0.3855, 0.5247, 0.6750, 0.8423, 1.0375, 1.2832, 1.6479, 1.9647, 2.3338, 2.5857, 3.3101,
         0.0627, 0.1257, 0.2534, 0.3855, 0.5246, 0.6748, 0.8421, 1.0371, 1.2826, 1.6468, 1.9629, 2.3310, 2.5820, 3.3027,
         0.0627, 0.1257, 0.2534, 0.3854, 0.5246, 0.6747, 0.8420, 1.0370, 1.2824, 1.6464, 1.9623, 2.3301, 2.5808, 3.3003]

    liberdade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 400, 500, 800, 1000]
    grauconf = [0.95, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, 0.05, 0.02, 0.01, 0.001]

    x = 0
    y = 0
    for i in range(len(liberdade)):
        if n == liberdade[i]:
            y = i
            break
        elif n < liberdade[i]:
            y = i-1
            break
    for i in range(len(grauconf)):
        if confianca == grauconf[i]:
            x = i
            break
        elif confianca > grauconf[i]:
            x = i-1
            break
    return tstudent[y*14+x]



def icNormal(dpp, n, media, significancia):
    significancia = float(significancia/200)

    z = tabelaNormal(significancia)

    ic = media - (z*dpp/float(sqrt(n)))
    ic2 = media + (z * dpp / float(sqrt(n)))

    resultado = (('ic', ic), ('ic2', ic2))
    return resultado

def icStudent(dp, n, media, significancia):
    confianca = float((100-significancia)/100)

    t = tabelaStudent(confianca, (n-1))

    ic = media - (t*dp/float(sqrt(n)))
    ic2 = media + (t*dp/float(sqrt(n)))

    resultado = (('ic', ic), ('ic2', ic2))
    return resultado

def pPopulacional(sucesso, tamanho, signficancia):
    signficancia = float(signficancia/200)

    z = tabelaNormal(signficancia)
    p = sucesso/tamanho

    ic = p - (z * sqrt(p * (1 - p) / tamanho))
    ic2 = p + (z * sqrt(p * (1 - p) / tamanho))

    resultado = (('ic', ic), ('ic2', ic2))
    return resultado

