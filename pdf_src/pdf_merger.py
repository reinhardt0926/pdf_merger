"""
PDF 병합 기능을 제공하는 모듈
"""
import os
from PyPDF2 import PdfMerger

class PDFMerger:
    """PDF 파일을 병합하는 클래스"""
    
    @staticmethod
    def merge_pdf_files(pdf_files, output_file, progress_callback=None):
        """
        여러 PDF 파일을 하나로 병합합니다.
        
        Args:
            pdf_files (list): 병합할 PDF 파일 경로 목록
            output_file (str): 병합된 PDF를 저장할 경로
            progress_callback (callable, optional): 진행 상태를 보고받을 콜백 함수
        
        Returns:
            bool: 병합 성공 여부
        
        Raises:
            Exception: PDF 병합 중 오류가 발생한 경우
        """
        if len(pdf_files) < 1:
            raise ValueError("병합할 PDF 파일이 필요합니다.")
        
        merger = PdfMerger()
        
        try:
            # 각 파일 병합
            total_files = len(pdf_files)
            for i, file in enumerate(pdf_files):
                if not os.path.exists(file):
                    raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file}")
                
                merger.append(file)
                
                # 진행 상황 보고
                if progress_callback:
                    progress = (i + 1) / total_files * 100
                    progress_callback(i + 1, total_files, progress)
            
            # 병합된 파일 저장
            merger.write(output_file)
            merger.close()
            return True
            
        except Exception as e:
            # 리소스 정리
            if merger:
                merger.close()
            raise e