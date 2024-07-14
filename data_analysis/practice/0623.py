import pandas as pd
import os

def calculate_averages(df):
    # データ範囲を取得
    data = df.values

    sum1, sum2, sum3 = 0, 0, 0
    count_rows = 0

    # 結果を出力するためのリスト
    results = []

    for i in range(len(data)):
        # 現在の行が "count" で始まるかチェック
        if isinstance(data[i][0], str) and data[i][0].startswith("count:"):
            if count_rows > 0:
                # 平均値を計算して結果リストに追加
                results.append([
                    sum1 / count_rows, 
                    sum2 / count_rows, 
                    sum3 / count_rows
                ])
            # 次のブロックのために変数をリセット
            sum1, sum2, sum3 = 0, 0, 0
            count_rows = 0
        else:
            # 各列の値を加算
            sum1 += float(data[i][0])
            sum2 += float(data[i][1])
            sum3 += float(data[i][2])
            count_rows += 1

    # 最後のブロックの平均値を計算して追加（ファイルの最後に count: がない場合）
    if count_rows > 0:
        results.append([
            sum1 / count_rows, 
            sum2 / count_rows, 
            sum3 / count_rows
        ])

    # 結果をデータフレームに変換
    results_df = pd.DataFrame(results, columns=['Average1', 'Average2', 'Average3'])
    return results_df

# .txtファイルからデータを読み込む
def read_txt_to_dataframe(file_path):
    # ファイルを読み込み、各行をリストに格納
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    # 各行をカンマで分割してデータフレームに変換
    data = [line.strip().split(',') for line in lines]

    # データフレームに変換
    df = pd.DataFrame(data)
    return df

# フォルダ内の全ての.txtファイルを処理
def process_all_files_in_folder(folder_path):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            df = read_txt_to_dataframe(file_path)
            results_df = calculate_averages(df)
            results[filename] = results_df
    return results

# サンプルフォルダパス
folder_path = r"C:\Users\takaharayota\Research\data\0623\1exp_withsound\0"

# フォルダ内の全ファイルを処理
results = process_all_files_in_folder(folder_path)

# 結果を表示
for filename, result_df in results.items():
    print(f"Results for {filename}:")
    print(result_df)
    print("\n")
