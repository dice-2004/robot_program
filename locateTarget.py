import cv2
import numpy as np

def preprocess(imInput):
	# 入力画像をHSVに変換し、平滑化
	imInputHSV = cv2.cvtColor(imInput, cv2.COLOR_BGR2HSV)
	imGaussianHSV = cv2.blur(imInputHSV, (3, 3))

	# RGB用に平滑化した画像も返す
	imGaussianRGB = cv2.blur(imInput, (3, 3))

	return imGaussianHSV, imGaussianRGB

# ゴール（黄）
def locateFlag(imInputHSV):
	# 対象色の定義（黄の場合）
	vMinHSV = np.array([20,127,0])
	vMaxHSV = np.array([35,255,255])
	imYellow = cv2.inRange(imInputHSV, vMinHSV, vMaxHSV)

	# 対象色のエリア画像の作成
	imYellowBinary = imYellow / 255

	# 対象色エリア（最も縦に長いもの）の水平位置の割り出し
	vSumYellowVertical = np.sum(imYellowBinary, axis=0)
	sMaxIndex = vSumYellowVertical.argmax()

	# 対象色エリアの縦の長さが5画素よりも大きい場合、ターゲットに設定
	if vSumYellowVertical[sMaxIndex] > 50:
		print("targetd yellow")
		sHorizontal = sMaxIndex
		sVertical = -1
		sSize = vSumYellowVertical[sMaxIndex]
	else:
		print("non targetd yellow")
		sHorizontal = -1
		sVertical = -1
		sSize = -1

	return (sHorizontal, sVertical, sSize), imYellowBinary

# 敵（赤）
def locateEnemy(imInputHSV):
	# 対象色の定義１（赤の場合）
	vMinHSV = np.array([0,180,0])
	vMaxHSV = np.array([10,255,255])
	imRed1 = cv2.inRange(imInputHSV, vMinHSV, vMaxHSV)

	# 対象色の定義２（赤の場合は色相が最大と最小に分かれるため2つ必要）
	vMinHSV = np.array([160,180,0])
	vMaxHSV = np.array([180,255,255])
	imRed2 = cv2.inRange(imInputHSV, vMinHSV, vMaxHSV)

	# 対象色のエリア画像の作成
	imRed = imRed1 + imRed2
	imRedBinary = imRed / 255

	# 対象色エリア（最も縦に長いもの）の水平位置の割り出し
	vSumRedVertical = np.sum(imRedBinary, axis=0)
	sMaxIndex = vSumRedVertical.argmax()

	# 対象色エリアの縦の長さが5画素よりも大きい場合、ターゲットに設定
	if vSumRedVertical[sMaxIndex] > 50:
		print("targetd red")
		sHorizontal = sMaxIndex
		sVertical = -1
		sSize = vSumRedVertical[sMaxIndex]
	else:
		print("non targetd red")
		sHorizontal = -1
		sVertical = -1
		sSize = -1

	return (sHorizontal, sVertical, sSize), imRedBinary


# 障害物（青）
def locateTarget(imInputHSV):
	# 対象色の定義（青の場合）
	vMinHSV = np.array([90,180,0])
	vMNaxHSV = np.array([150,255,255])
	imBlue = cv2.inRange(imInputHSV, vMinHSV, vMNaxHSV)
	# 対象色のエリア画像の作成
	imBlueBinary = imBlue / 255
	# 対象色エリア（最も縦に長いもの）の水平位置の割り出し
	vSumBlueVertical = np.sum(imBlueBinary, axis=0)
	sMaxIndex = vSumBlueVertical.argmax()
	# 対象色エリアの縦の長さが5画素よりも大きい場合、ターゲットに設定
	if vSumBlueVertical[sMaxIndex] > 5:
		print("targetd blue")
		sHorizontal = sMaxIndex
		sVertical = -1
		sSize = vSumBlueVertical[sMaxIndex]
	else:
		print("non targetd blue")
		sHorizontal = -1
		sVertical = -1
		sSize = -1
	return (sHorizontal, sVertical, sSize), imBlueBinary

def locateCylinder(imInputRGB):
	# 対象色の定義（緑の場合 - RGB）
	# BGR形式なので、[B, G, R]の順
	vMinRGB = np.array([0, 100, 0])    # 最小値: B=0, G=100, R=0
	vMaxRGB = np.array([100, 255, 100]) # 最大値: B=100, G=255, R=100
	imGreen = cv2.inRange(imInputRGB, vMinRGB, vMaxRGB)

	# 対象色のエリア画像の作成
	imGreenBinary = imGreen / 255

	# 対象色エリア（最も縦に長いもの）の水平位置の割り出し
	vSumGreenVertical = np.sum(imGreenBinary, axis=0)
	sMaxIndex = vSumGreenVertical.argmax()

	# 対象色エリアの縦の長さが5画素よりも大きい場合、ターゲットに設定
	if vSumGreenVertical[sMaxIndex] > 30:
		print("targetd green")
		sHorizontal = sMaxIndex
		sVertical = -1
		sSize = vSumGreenVertical[sMaxIndex]
	else:
		print("non targetd green")
		sHorizontal = -1
		sVertical = -1
		sSize = -1

	return (sHorizontal, sVertical, sSize), imGreenBinary
