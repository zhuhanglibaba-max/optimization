#!/usr/bin/env python3
"""
从 Kaggle 下载 ImageNet 数据集的脚本

使用前需要：
1. 安装 kaggle: pip install kaggle
2. 配置 Kaggle API 凭证：
   - 访问 https://www.kaggle.com/settings 获取 API token
   - 下载 kaggle.json 文件
   - 将 kaggle.json 放在 ~/.kaggle/ 目录下
   - 设置权限: chmod 600 ~/.kaggle/kaggle.json
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

def check_kaggle_installed():
    """检查是否安装了 kaggle 包"""
    try:
        import kaggle
        return True
    except ImportError:
        return False

def check_kaggle_credentials():
    """检查 Kaggle API 凭证是否配置"""
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_json = kaggle_dir / 'kaggle.json'
    
    if not kaggle_json.exists():
        return False, "未找到 kaggle.json 文件"
    
    # 检查文件权限
    stat_info = os.stat(kaggle_json)
    mode = stat_info.st_mode
    if mode & 0o077 != 0:
        return False, "kaggle.json 文件权限不安全（应为 600）"
    
    return True, "凭证配置正确"

def setup_kaggle_credentials():
    """设置 Kaggle API 凭证"""
    print("\n" + "=" * 60)
    print("配置 Kaggle API 凭证")
    print("=" * 60)
    print("\n请按照以下步骤操作：")
    print("\n1. 访问 https://www.kaggle.com/settings")
    print("2. 在 'API' 部分，点击 'Create New Token'")
    print("3. 下载 kaggle.json 文件")
    print("4. 将文件移动到 ~/.kaggle/ 目录：")
    print("   mkdir -p ~/.kaggle")
    print("   mv ~/Downloads/kaggle.json ~/.kaggle/")
    print("5. 设置文件权限：")
    print("   chmod 600 ~/.kaggle/kaggle.json")
    print("\n" + "=" * 60)

def download_imagenet_kaggle(dataset_name, output_dir, unzip=True):
    """
    从 Kaggle 下载 ImageNet 数据集
    
    Args:
        dataset_name: Kaggle 数据集名称，例如 'c/imagenet-object-localization-challenge'
        output_dir: 输出目录
        unzip: 是否自动解压
    """
    print("\n" + "=" * 60)
    print(f"开始从 Kaggle 下载 ImageNet 数据集")
    print("=" * 60)
    print(f"数据集: {dataset_name}")
    print(f"输出目录: {output_dir}")
    print("=" * 60)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # 使用 kaggle API 下载
        cmd = ['kaggle', 'datasets', 'download', '-d', dataset_name, '-p', output_dir]
        
        if unzip:
            cmd.append('--unzip')
        
        print(f"\n执行命令: {' '.join(cmd)}")
        print("\n开始下载（这可能需要较长时间，请耐心等待）...")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("\n" + "=" * 60)
        print("✓ 下载完成！")
        print("=" * 60)
        print(f"\n数据集保存位置: {output_dir}")
        
        if unzip:
            print("文件已自动解压")
        else:
            print("文件为 ZIP 格式，需要手动解压")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 下载失败: {e}")
        print(f"错误输出: {e.stderr}")
        
        if "401" in str(e.stderr) or "Unauthorized" in str(e.stderr):
            print("\n" + "=" * 60)
            print("认证失败！请检查 Kaggle API 凭证")
            print("=" * 60)
            setup_kaggle_credentials()
        elif "404" in str(e.stderr) or "not found" in str(e.stderr).lower():
            print("\n" + "=" * 60)
            print("数据集未找到！")
            print("=" * 60)
            print("请检查数据集名称是否正确")
            print("常见 ImageNet 数据集：")
            print("  - imagenet-object-localization-challenge")
            print("  - imagenet-object-localization-challenge/ILSVRC")
            print("\n访问 https://www.kaggle.com/datasets 搜索 'imagenet' 查找正确的数据集名称")
        
        return False
    except FileNotFoundError:
        print("\n❌ 未找到 kaggle 命令")
        print("请先安装: pip install kaggle")
        return False
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='从 Kaggle 下载 ImageNet 数据集',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 下载 ImageNet 对象定位挑战数据集
  python download_imagenet_kaggle.py --dataset imagenet-object-localization-challenge --output_dir ./datasets/imagenet
  
  # 下载但不自动解压
  python download_imagenet_kaggle.py --dataset imagenet-object-localization-challenge --output_dir ./datasets/imagenet --no-unzip
  
  # 使用完整数据集路径
  python download_imagenet_kaggle.py --dataset c/imagenet-object-localization-challenge --output_dir ./datasets/imagenet

常见 ImageNet 数据集名称:
  - imagenet-object-localization-challenge (ILSVRC 2012)
  - imagenet-object-localization-challenge/ILSVRC/Data/CLS-LOC
  
注意:
  1. 首次使用需要配置 Kaggle API 凭证
  2. 访问 https://www.kaggle.com/settings 获取 API token
  3. 将 kaggle.json 放在 ~/.kaggle/ 目录下
  4. ImageNet 数据集很大（约 150GB），确保有足够的磁盘空间和稳定的网络连接
        """
    )
    
    parser.add_argument(
        '--dataset',
        type=str,
        default='imagenet-object-localization-challenge',
        help='Kaggle 数据集名称 (默认: imagenet-object-localization-challenge)'
    )
    
    parser.add_argument(
        '--output_dir',
        type=str,
        default='./datasets/imagenet',
        help='输出目录 (默认: ./datasets/imagenet)'
    )
    
    parser.add_argument(
        '--no-unzip',
        action='store_true',
        help='不自动解压 ZIP 文件'
    )
    
    parser.add_argument(
        '--setup',
        action='store_true',
        help='显示 Kaggle API 凭证配置说明'
    )
    
    args = parser.parse_args()
    
    # 如果只是显示配置说明
    if args.setup:
        setup_kaggle_credentials()
        return
    
    # 检查 kaggle 是否安装
    if not check_kaggle_installed():
        print("\n❌ 未安装 kaggle 包")
        print("\n请先安装:")
        print("  pip install kaggle")
        print("\n或者添加到 requirements.txt 后运行:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    
    # 检查凭证配置
    credentials_ok, message = check_kaggle_credentials()
    if not credentials_ok:
        print(f"\n⚠ {message}")
        setup_kaggle_credentials()
        
        # 询问是否继续
        response = input("\n是否已配置好凭证并继续下载？(y/n): ")
        if response.lower() != 'y':
            print("已取消")
            sys.exit(0)
    
    # 下载数据集
    success = download_imagenet_kaggle(
        args.dataset,
        args.output_dir,
        unzip=not args.no_unzip
    )
    
    if success:
        print("\n" + "=" * 60)
        print("下载完成！")
        print("=" * 60)
        print(f"\n数据集位置: {args.output_dir}")
        print("\n提示: ImageNet 数据集很大，解压可能需要较长时间")
    else:
        print("\n" + "=" * 60)
        print("下载失败，请检查错误信息并重试")
        print("=" * 60)
        sys.exit(1)

if __name__ == '__main__':
    main()
