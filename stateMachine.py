# 状態定義 ----------------------------------------------------
IDLE = 0
FORWARD = 1
BACKWARD = 2
RIGHT = 3
LEFT = 4

# ステートマシン -------------------------------------------------

def stateMachine(sState, vFlagInfo, vEnemyInfo,vTargetInfo, vCylinderInfo):


    #Infoの書式: (sHorizontal(水平位置), sVertical(垂直位置※今回は常に-1), sSize(縦の長さ))
    #Flag:ゴール　enemy:よける対象　target:左側を通らなければならない対象　cylinder:円柱（よける対象）
    sHorizontalCenter = 160
    sPositionThreshHigh = 15
    sPositionThreshLow = 5
    sSizeThreshHigh = 80
    sSizeThreshLow = 5

    if sState == IDLE:
        # Targetが視野に入っている場合,優先して対応
        # 青　障害物
        if vTargetInfo[0] != -1:
            # Targetが右に無い場合、左に旋回
            if vTargetInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Targetが右にある場合、直進
            elif vTargetInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 緑　棒（右側を通る：青の逆）
        elif vCylinderInfo[0] != -1:
            # Cylinderが左に無い場合、右に旋回
            if vCylinderInfo[0] > sHorizontalCenter - sPositionThreshHigh * 3:
                sState = RIGHT
            # Cylinderが左にある場合、直進
            elif vCylinderInfo[0] < sHorizontalCenter - sPositionThreshHigh * 3:
                sState = FORWARD
        # 赤　敵（左側を通る：青と同じ）
        elif vEnemyInfo[0] != -1:
            # Enemyが右に無い場合、左に旋回
            if vEnemyInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Enemyが右にある場合、直進
            elif vEnemyInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 黄　ゴール
        elif vFlagInfo[0] != -1 and vFlagInfo[2] < sSizeThreshHigh:
            sState = FORWARD

    elif sState == FORWARD:
        # Targetが視野に入っている場合,優先して対応
        # 青　障害物
        if vTargetInfo[0] != -1:
            # Targetが右に無い場合、左に旋回
            if vTargetInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Targetが右にある場合、直進
            elif vTargetInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 緑　棒（右側を通る：青の逆）
        elif vCylinderInfo[0] != -1:
            # Cylinderが左に無い場合、右に旋回
            if vCylinderInfo[0] > sHorizontalCenter - sPositionThreshHigh * 3:
                sState = RIGHT
            # Cylinderが左にある場合、直進
            elif vCylinderInfo[0] < sHorizontalCenter - sPositionThreshHigh * 3:
                sState = FORWARD
        # 赤　敵（左側を通る：青と同じ）
        elif vEnemyInfo[0] != -1:
            # Enemyが右に無い場合、左に旋回
            if vEnemyInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Enemyが右にある場合、直進
            elif vEnemyInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 黄　ゴール
        elif vFlagInfo[0] != -1:
            if vFlagInfo[0] > sHorizontalCenter + sPositionThreshHigh:
                sState = RIGHT
            elif vFlagInfo[0] < sHorizontalCenter - sPositionThreshHigh:
                sState = LEFT
            elif vFlagInfo[2] < sSizeThreshLow or vFlagInfo[2] > sSizeThreshHigh or vFlagInfo[0] == -1:
                sState = FORWARD


    elif sState == RIGHT:
        #targetが視野に入っている場合,優先して対応
        # 青　障害物
        if vTargetInfo[0] != -1:
            #targetが右に無い場合、左に旋回
            if vTargetInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            #targetが右にある場合、直進
            elif vTargetInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 緑　棒（右側を通る：青の逆）
        elif vCylinderInfo[0] != -1:
            # Cylinderが左に無い場合、右に旋回
            if vCylinderInfo[0] > sHorizontalCenter - sPositionThreshHigh * 3:
                sState = RIGHT
            # Cylinderが左にある場合、直進
            elif vCylinderInfo[0] < sHorizontalCenter - sPositionThreshHigh * 3:
                sState = FORWARD
        # 赤　敵（左側を通る：青と同じ）
        elif vEnemyInfo[0] != -1:
            # Enemyが右に無い場合、左に旋回
            if vEnemyInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Enemyが右にある場合、直進
            elif vEnemyInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 黄　ゴール
        elif vFlagInfo[0] != -1:
            if vFlagInfo[0] < sHorizontalCenter + sPositionThreshLow:
                sState = FORWARD
            elif vFlagInfo[2] < sSizeThreshLow or vFlagInfo[2] > sSizeThreshHigh or vFlagInfo[0] == -1:
                sState = FORWARD

    elif sState == LEFT:
        #targetが視野に入っている場合,優先して対応
        # 青　障害物
        if vTargetInfo[0] != -1:
            #targetが右に無い場合、左に旋回
            if vTargetInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            #targetが右にある場合、直進
            elif vTargetInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 緑　棒（右側を通る：青の逆）
        elif vCylinderInfo[0] != -1:
            # Cylinderが左に無い場合、右に旋回
            if vCylinderInfo[0] > sHorizontalCenter - sPositionThreshHigh * 3:
                sState = RIGHT
            # Cylinderが左にある場合、直進
            elif vCylinderInfo[0] < sHorizontalCenter - sPositionThreshHigh * 3:
                sState = FORWARD
        # 赤　敵（左側を通る：青と同じ）
        elif vEnemyInfo[0] != -1:
            # Enemyが右に無い場合、左に旋回
            if vEnemyInfo[0] < sHorizontalCenter + sPositionThreshHigh * 3:
                sState = LEFT
            # Enemyが右にある場合、直進
            elif vEnemyInfo[0] > sHorizontalCenter + sPositionThreshHigh * 3:
                sState = FORWARD
        # 黄　ゴール
        elif vFlagInfo[0] != -1:
            if vFlagInfo[0] > sHorizontalCenter - sPositionThreshLow:
                sState = FORWARD
            elif vFlagInfo[2] < sSizeThreshLow or vFlagInfo[2] > sSizeThreshHigh or vFlagInfo[0] == -1:
                sState = FORWARD

    return sState
