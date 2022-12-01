
# 파편화된 데이터의 적극 활용을 위한 시계열 기반 통합 플랫폼 기술 개발

- 참여 기관명 : 광운대학교, 신경공학 및 인공지능 연구실(NeuroAI Lab)

- 연구책임자 : 최영석 교수

- 개발자 정보
  - 김채민 연구원
  - Email : k9is@kw.ac.kr 

- 참여 기관 실무 담당자 및 작성자 정보
  - 김대현 연구원
  - Email : 
  - 이현규 연구원
  - Email : skgusrb12@kw.ac.kr 

## 1. Introduction

- **엔트로피(Entropy) 기법을 활용한 시계열 데이터의 비정규성(irregularity) 및 randomness 정량화 기술 개발**

- **개발 기술 요약** 

|제안 기법|기능|활용 예제|
|:--------:|:-------:|:------:|
|멀티 스케일 엔트로피 (Multiscale Entropy)|  시계열 데이터 기반의 정상/비정상(이상 데이터) 특징 추출 및 상황 감지| 심박변이율의 복잡도를 다양한 스케일에서 분석하여 울혈성 심부전 환자와 정상인 데이터를 구분하기 위함



## 2. Sample Dataset (Input Data Formats)

- PhysioNet(https://physionet.org)에서 제공되는 울혈성 심부전증(BIDMC CHF, CHFDB) 환자 데이터가 활용되었으며, 입력 데이터는 실험자 수 x 데이터 길이(S x N)로 구성됨.

- S : 1 x N 크기의 시계열 데이터의 개수
- N : 데이터 길이

## 3. Multiscale Entropy Method
#####  1. MDE : Multiscale Dispersion Entropy
##### 2. MCRDE :   Multiscale Cumulative Residual Dispersion Entropy
##### 3. MFDE :   Multiscale Fuzzy Dispersion Entropy

## 4. Parameter
*   in main.py
	 #### Multiscale Entropy Method parameter
	```python
	Entropy_method : Multiscale Entropy method
	(ex. Entropy_method = 'MCRDE')
	```
	- Entropy_method : 사용하고자 하는 Multiscale Entropy 		 method를 문자열로 입력 { 'MDE', 'MCRDE', 'MFDE' }
	
    #### MDE Parameter
	```python
	N : 데이터 길이 (default: 1000)
	m : 데이터 차원 수 (default: 3)
	c : 클래스 수 (default: 6)		                
	tau : 지연 인자 (default: 1)
	scale : 스케일 수 (default: 25)
	params_dict : { 'N':N,'m':m,'c':c,'tau':tau,'scale':scale } (type:dict) 
	```
  	- m :  'm' 개의 인자를 가지는 분산 패턴 (dispersion pattern) 생성
	- c : 분산 패턴을 생성할 때 각 인자는 1부터 c 까지의 정수로 맵핑됨
	- tau : 데이터를 맵핑하는 간격 
	- scale : Multiscale entropy 계산을 위해서 필요, 새로운 시계열 형성을 위해 원래의 시계열을 묶는 단위
	- default : N=1000,m=3,c=6,tau=1,scale=25
	
	 #### MCRDE Parameter
	- MDE와 동일한 파라미터 사용 : { N, m, c, tau, scale }
	- default : N=1000,m=3,c=6,tau=1,scale=25
	 #### MFDE Parameter
	- MDE와 동일한 파라미터 사용 : { N, m, c, tau, scale } 
	- default : N=1000,m=4,c=4,tau=1,scale=25
	
	
	
## 5. Usage

### `Main.py` 



- **Output Data Formats**
	```python
	Entropy_chf     = np.zeros((n_s, scale))
	Entropy_healthy = np.zeros((n_s, scale)) 
	```
  - n_s : 데이터의 수
  - scale : 스케일 인자의 수
  - example) Entropy_chf(3,15) : 3번째 CHF 피험자의 scale 15에서의 엔트로피 값 ('Multiscale Entropy method'를 통해 정량화된 수치)

	
	
- **Calculate Multiscale Entropy Value**

  ```python
  for i in range(n_s):  
    Entropy_chf[i] = Entropy_method_dict[Entropy_method](RRIs_CHF_1000[i, :N], params_dict)  
    Entropy_healthy[i] = Entropy_method_dict[Entropy_method](RRIs_HEALTHY_1000[i, :N], params_dict)  
  
  avg_Entropy_chf = np.mean(Entropy_chf, axis=0)  
  avg_Entropy_healthy = np.mean(Entropy_healthy, axis=0)  
    
  std_Entropy_chf = np.std(Entropy_chf, axis=0)  
  std_Entropy_healthy = np.std(Entropy_healthy, axis=0)
  ```
  - avg_Entropy_chf : 전체 울혈성 심부전증  피험자 데이터에 대한 Entropy 평균 (열은 스케일을 의미)
  - avg_Entropy_healthy : 전체 건강한 피험자 데이터에 대한 Entropy 평균 (열은 스케일을 의미)
  - std_Entropy_chf : 전체 울혈성 심부전증 피험자 데이터에 대한 Entropy 표준편차 (열은 스케일을 의미)
  - std_Entropy_healthy : 전체 건강한 피험자  데이터에 대한 Entropy 표준편차 (열은 스케일을 의미)

  

-	**결과 저장 (Multiscale Entropy의 평균 및 표준편차)**
	
	```python 
	write_txt(Entropy_method, scale,
			 avg_Entropy_chf_path, avg_Entropy_healthy_path,
	         std_Entropy_chf_path, std_Entropy_healthy_path,
	         avg_Entropy_chf, avg_Entropy_healthy,
	         std_Entropy_chf, std_Entropy_healthy)
	```
	-  example) 전체 울혈성 심부전증 피험자 데이터에 대한 MCRDE 평균값 
	path : results/avg_MCRDE_chf.txt

	   <img src="https://github.com/piggymouse/MCRDE-report/blob/main/MCRDE_value.jpg?raw=true" width=300> 



## 6. Results

-  **Figure parameter**

	  ```python
	if show_fig == True:
	    Entropy = plot_Entropy(Entropy_method,
								  subject,
								  plt_color,
								  plt_marker,
								  plt_linestyle,
	                            avg_Entropy_chf,
	                            avg_Entropy_healthy,
	                            std_Entropy_chf,
	                            std_Entropy_healthy,
	                            pCHF_HT,
	                            params_dict)
	```
	
	 - Entropy_method: Multiscale Entropy method   
	 - subject: 그래프의 legend
	 - plt_color: 그래프의 색상
	 - plt_marker: 그래프의 마커
	 - plt_linestyle: 그래프의 라인 스타일
	 - avg_Entropy_~:  Entropy 평균
	 - std_Entropy_~:  Entropy 표준 편차 
	 - scale: 스케일 인자의 수
	 - pCHF_HT: 울혈성 심부전증 피험자 (CHF) 와 건강한 피험자 (Healthy) 사이의 p value
	 - param_dict: Multiscale Entropy method에 대한 파라미터 값을  dictionary 형태로 저장
	  ex) ``` python
	  params_dict = {'N':N,'m':m,'c':c,'tau':tau,'scale':scale}  ```
	
		
- **MCRDE 결과 그래프**

	![Figure_1](https://github.com/piggymouse/MCRDE-report/blob/main/MCRDE%20plot_20220722.png?raw=true)


	* 데이터의 길이(N): 1000
	 * x 축: Scale factor 
	 * y 축: Entropy Value 
	 * MCRDE의 평균: 마커 ('o', '^')로 표시
	 * MCRDE의 표준편차: 에러바로 표시
	 *  에러바 위의 '*' 표시는 해당  스케일에서 두 데이터(CHF, HEALTHY)가 유의 수준 (p-value<0.05) 에서 서로 독립적인 것을 의미
	 
       
    



