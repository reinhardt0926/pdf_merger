"""
PDF 합치기 애플리케이션의 사용자 인터페이스
"""
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_src.pdf_merger import PDFMerger

class PDFMergerApp:
    """PDF 합치기 애플리케이션의 GUI 클래스"""
    
    def __init__(self, root):
        """
        PDFMergerApp 초기화
        
        Args:
            root: Tkinter 루트 윈도우
        """
        self.root = root
        self.root.title("PDF 파일 병합 프로그램")
        self.root.geometry("600x400")
        self.root.minsize(500, 350)
        
        # 종료 시 확인 다이얼로그
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # 파일 목록 초기화
        self.pdf_files = []
        
        # UI 설정
        self.setup_ui()
    
    def setup_ui(self):
        """UI 컴포넌트 초기화 및 배치"""
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 버튼 프레임
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        # 파일 추가 버튼
        add_btn = ttk.Button(btn_frame, text="PDF 파일 추가", command=self.add_files)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # 선택 파일 제거 버튼
        remove_btn = ttk.Button(btn_frame, text="선택 파일 제거", command=self.remove_selected)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        # 모든 파일 제거 버튼
        clear_btn = ttk.Button(btn_frame, text="모든 파일 제거", command=self.clear_files)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # 병합 버튼
        merge_btn = ttk.Button(btn_frame, text="PDF 병합하기", command=self.merge_pdfs)
        merge_btn.pack(side=tk.RIGHT, padx=5)
        
        # 파일 목록 프레임
        list_frame = ttk.LabelFrame(self.main_frame, text="PDF 파일 목록")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 스크롤바 생성
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 리스트박스 생성
        self.file_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)
        
        # 스크롤바와 리스트박스 연결
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_listbox.yview)
        
        # 파일 순서 이동 버튼 프레임
        order_frame = ttk.Frame(self.main_frame)
        order_frame.pack(fill=tk.X, pady=5)
        
        # 위로 이동 버튼
        up_btn = ttk.Button(order_frame, text="↑ 위로", command=self.move_up)
        up_btn.pack(side=tk.LEFT, padx=5)
        
        # 아래로 이동 버튼
        down_btn = ttk.Button(order_frame, text="↓ 아래로", command=self.move_down)
        down_btn.pack(side=tk.LEFT, padx=5)
        
        # 상태 표시줄
        self.status_var = tk.StringVar()
        self.status_var.set("준비됨")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def add_files(self):
        """PDF 파일 추가 대화상자 표시"""
        files = filedialog.askopenfilenames(
            title="PDF 파일 선택",
            filetypes=[("PDF 파일", "*.pdf")]
        )
        
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    self.file_listbox.insert(tk.END, os.path.basename(file))
            
            self.status_var.set(f"{len(files)}개 파일이 추가되었습니다.")
    
    def remove_selected(self):
        """선택된 파일 제거"""
        selected_indices = self.file_listbox.curselection()
        
        if not selected_indices:
            messagebox.showwarning("경고", "제거할 파일을 선택하세요.")
            return
        
        # 인덱스를 역순으로 정렬하여 삭제 시 인덱스 변화 방지
        for index in sorted(selected_indices, reverse=True):
            self.file_listbox.delete(index)
            self.pdf_files.pop(index)
        
        self.status_var.set(f"{len(selected_indices)}개 파일이 제거되었습니다.")
    
    def clear_files(self):
        """모든 파일 제거"""
        self.file_listbox.delete(0, tk.END)
        self.pdf_files.clear()
        self.status_var.set("모든 파일이 제거되었습니다.")
    
    def move_up(self):
        """선택한 파일을 목록에서 위로 이동"""
        selected_indices = self.file_listbox.curselection()
        
        if not selected_indices:
            messagebox.showwarning("경고", "이동할 파일을 선택하세요.")
            return
        
        for index in selected_indices:
            if index > 0:
                # 파일 목록과 리스트박스 항목 교환
                self.pdf_files[index], self.pdf_files[index-1] = self.pdf_files[index-1], self.pdf_files[index]
                file_text = self.file_listbox.get(index)
                self.file_listbox.delete(index)
                self.file_listbox.insert(index-1, file_text)
                self.file_listbox.selection_set(index-1)
    
    def move_down(self):
        """선택한 파일을 목록에서 아래로 이동"""
        selected_indices = self.file_listbox.curselection()
        
        if not selected_indices:
            messagebox.showwarning("경고", "이동할 파일을 선택하세요.")
            return
        
        # 역순으로 처리하여 다중 선택 시 올바르게 동작하도록 함
        for index in sorted(selected_indices, reverse=True):
            if index < len(self.pdf_files) - 1:
                # 파일 목록과 리스트박스 항목 교환
                self.pdf_files[index], self.pdf_files[index+1] = self.pdf_files[index+1], self.pdf_files[index]
                file_text = self.file_listbox.get(index)
                self.file_listbox.delete(index)
                self.file_listbox.insert(index+1, file_text)
                self.file_listbox.selection_set(index+1)
    
    def merge_pdfs(self):
        """PDF 파일 병합 실행"""
        if len(self.pdf_files) < 2:
            messagebox.showwarning("경고", "병합할 PDF 파일을 2개 이상 추가하세요.")
            return
        
        # 저장 파일 경로 선택
        output_file = filedialog.asksaveasfilename(
            title="병합된 PDF 저장",
            defaultextension=".pdf",
            filetypes=[("PDF 파일", "*.pdf")]
        )
        
        if not output_file:
            return
        
        try:
            # 진행 상황 창 생성
            progress_window = tk.Toplevel(self.root)
            progress_window.title("병합 진행 중")
            progress_window.geometry("300x100")
            progress_window.resizable(False, False)
            progress_window.transient(self.root)
            progress_window.grab_set()
            
            # 진행 상황 표시 라벨
            progress_label = ttk.Label(progress_window, text="PDF 파일 병합 중...")
            progress_label.pack(pady=10)
            
            # 진행 상황 표시 바
            progress_bar = ttk.Progressbar(progress_window, length=250, mode="determinate")
            progress_bar.pack(pady=10)
            
            # 진행 상황 업데이트 콜백 함수
            def update_progress(current, total, progress):
                progress_bar["value"] = progress
                progress_label.config(text=f"PDF 파일 병합 중... ({current}/{total})")
                progress_window.update()
            
            # PDF 병합 실행
            pdf_merger = PDFMerger()
            result = pdf_merger.merge_pdf_files(self.pdf_files, output_file, update_progress)
            
            progress_window.destroy()
            
            if result:
                self.status_var.set(f"PDF 병합 완료: {os.path.basename(output_file)}")
                messagebox.showinfo("완료", f"PDF 파일이 성공적으로 병합되었습니다.\n저장 위치: {output_file}")
            
        except Exception as e:
            if 'progress_window' in locals() and progress_window.winfo_exists():
                progress_window.destroy()
            messagebox.showerror("오류", f"PDF 병합 중 오류가 발생했습니다.\n{str(e)}")
    
    def on_close(self):
        """애플리케이션 종료 확인"""
        if messagebox.askokcancel("종료", "PDF 병합 프로그램을 종료하시겠습니까?"):
            self.root.destroy()