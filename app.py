import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from object_detection import detect_object
import base64

    
#st.balloons()
# option = st.sidebar.radio("Menu",['Home', 'About','Contributors'])
st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Menu </h1>',
                    unsafe_allow_html=True)
option = st.sidebar.radio(" ",('Home', 'About Model','About Project','Contributors'))


if option == 'Home':
      
      col1,col2,col3 = st.columns([50,100,1])
    
      # col2.image('chapter-logo.jpg')
      st.markdown(
          """
          <style>
          .container1 {
          display: flex;
        }
        .logo-img1 {
             float:right;
             width:350px;
             height:350px;
             margin: 0px 0px 0px 170px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          """
          <style>
          .container2 {
          display: flex;
        }
        .img {
             float:right;
             width:300px;
             height:350px;
             margin: 0px 0px 0px 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          f"""
          <div class="container1">
               <img class="logo-img1" src="data:image/jpg;base64,{base64.b64encode(open('chapter-logo.jpg', "rb").read()).decode()}">
          </div>
          """,
          unsafe_allow_html=True
      )
      #st.title('Omdena - Ahmedabad Chapter')
      #st.header('Anamoly detection on Martian Surface')
      st.text("")
      st.text("")
      st.text("")
      html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Anomaly Detection On Martian Surface</h2>
        </div>
        """
      st.markdown(html_temp,unsafe_allow_html=True)
      st.text("")
      st.text("")
      st.text("")

      def upload_image_ui():
          uploaded_image = st.file_uploader("Please upload a martian surface image file", type=["png", "jpg", "jpeg"])
          if uploaded_image is not None:
            try:
                image = Image.open(uploaded_image)
                image = ImageOps.grayscale(image)
            except Exception:
                st.error("Error: Invalid image")
            else:
                img_array = np.array(image)
                return img_array
        
      img_array = upload_image_ui()
      st.text("")
      st.text("")

      if isinstance(img_array, np.ndarray):
        image, instances, conf = detect_object(img_array)
        st.image(image)
        for instance, confidence in zip(instances, conf):
              st.subheader("Our model is "+ str(round((confidence * 100), 2))+ "% sure that the image contains a " + instance.split(':')[0])
              st.text("")
        
      
      ana_type = st.sidebar.selectbox(
        "To know more about Anamolies ",
        ("Select an anamoly","Crater","Dark dune","Slope streak","Bright dune","Impact ejecta","Swiss cheese","Spider"))
        
      if ana_type == 'Crater':
            image1 = Image.open('Anamolies-images/craters.jpg')
            st.sidebar.image(image1, caption='Craters on Mars')
            st.sidebar.write("Craters are caused when a [bolide](https://en.wikipedia.org/wiki/Bolide) collides with a planet. The Martian surface contains thousands of impact craters because, unlike Earth, Mars has a stable crust, low erosion rate, and no active sources of lava")
      
      elif ana_type =='Dark dune':
            image2 = Image.open('Anamolies-images/dark-dunes.jpg')
            st.sidebar.image(image2, caption='Dark dunes on Mars')
            st.sidebar.write("The dunes within and around the crater are thought to contain sandy material rich in pyroxene and olivinew which are rock forming minerals that are mafic(containing Magnesium and Iron).")
            
      elif ana_type =='Slope streak':
            image3 = Image.open('Anamolies-images/slope-streak.jpg')
            st.sidebar.image(image3, caption='Slope streak on Mars')
            st.sidebar.write("Slope streaks are prevalent on the surface of the Mars, but they come in multitude of shapes and sizes.")
            
      elif ana_type =='Bright dune':
            image4 = Image.open('Anamolies-images/bright-dune.jpg')
            st.sidebar.image(image4, caption='Bright dune on Mars')
            st.sidebar.write("These martian dunes are brighter and are composed of possibly sulphates.")
      elif ana_type =='Impact ejecta':
            image5 = Image.open('Anamolies-images/impact-ejecta.jpg')
            st.sidebar.image(image5, caption='Impact ejecta on Mars')
            st.sidebar.write("Impact ejecta is a material that is thrown up and out of the surface of the planet as a result of the impact of an [meteorite](https://en.wikipedia.org/wiki/Meteorite), [asteroid](https://en.wikipedia.org/wiki/Asteroid) or [comet](https://en.wikipedia.org/wiki/Comet). The material that was originally beneath the surface of the planet then rains down onto the environs of the newly formed impact crater.")
     
      elif ana_type =='Swiss cheese':
            image6 = Image.open('Anamolies-images/swiss-cheese.jpg')
            st.sidebar.image(image6, caption='Swiss cheese on Mars')
            st.sidebar.write("The [Martian south polar cap](https://en.wikipedia.org/wiki/Martian_polar_ice_caps) is a layer of carbon dioxide ice, full of pits that make it look like Swiss cheese. The pits form when the Sun heats the ice and makes it sublimate (transform from a solid to a gas).")
      
      elif ana_type =='Spider':
            image7 = Image.open('Anamolies-images/spiders.jpg')
            st.sidebar.image(image7, caption='Spiders on Mars')
            st.sidebar.write("Spiders are actually topological troughs formed when dry ice directly sublimates to a gas.")
         



if option == 'About Model':
  html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Model Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.subheader("YOLOv4 Model Description: ")
  st.markdown('• The head(the part which handles prediction) of YOLOv4 contains Yolo v3',unsafe_allow_html=True)
  st.markdown('• CSPDarknet53 neural network is the backbone for YOLOv4 and Spatial pyramid pooling on the CSPDarknet53, was used as it separates out the most significant context features and causes almost no reduction of the network operation speed.',unsafe_allow_html=True)
  st.markdown('• PANet also known as Path aggregation network as the method of parameter aggregation from different backbone levels for different detector levels and it was use instead of the FPN also known as Feature Pyramid Network used in YOLOv3',unsafe_allow_html=True)
  st.markdown('• Various optimizations to the training method can be done to yield better accuracy without increasing the inference cost.',unsafe_allow_html=True)
  st.markdown('• For the backbone, the authors used data augmentation which is meant to increase the variability of the input images, so that the object detection model has higher robustness to the images obtained from different environments(which is in our case, Mars).',unsafe_allow_html=True)
  st.markdown('• The authors also  made additional design and improvement such as a new method of data augmentation called Mosaic, and Self-Adversarial Training (SAT) and also selected optimal hyper-parameters while applying genetic algorithms.',unsafe_allow_html=True)
  st.markdown('• NVIDIA 1080 TI and 2080 TI GPUs were used by the authors of YOLOv4 for training the datasets, ImageNet and MS-COCO.',unsafe_allow_html=True)
  st.markdown('• The following hyperparameters were used by them for ImageNet dataset:',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Training Epochs or iterations: 8 million',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Batch size: 128',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Mini batch size: 32',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Learning rate(using polynomial decay): 0.1',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Warm-up steps: 1000',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Momentum: 0.9',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Weight Decay: 0.005',unsafe_allow_html=True)
  st.markdown('• The following hyperparameters were used by them for MS-COCO dataset:',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Training Epochs or iterations: 500,500',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Batch size: 128',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Mini batch size: 32',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Learning rate(using step decay): 0.1',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Learn steps: learning steps were multiplied by a factor of 0.1 at 400,000 steps and 450,000 steps respectively.',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Momentum: 0.9',unsafe_allow_html=True)
  st.markdown('&nbsp; &nbsp; &nbsp; • Weight Decay: 0.005',unsafe_allow_html=True)
  st.markdown('• The authors also did an ablation study where one systematically removes parts of the input to see which parts of the input are relevant to the networks output.', unsafe_allow_html=True)
  st.markdown('• In a nutshell, YOLOv4 is faster in terms of Frames per Second (FPS) and more accurate on MS-COCO datasets than all available alternative detectors. So, YOLOv4 can be trained and used on a conventional GPU with 8-16GB VRAMs which are easily available.',unsafe_allow_html=True)

if option == 'About Project':
  html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Project Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")

if option == 'Contributors':
      harshal_IMAGE = "harshal.jpg"
      kanak_IMAGE = "kanak.jpg"
      tanisha_IMAGE = "tanisha.jpeg"
      vamsi_IMAGE = "vamsi.jpg"
      venkat_IMAGE = "venkat.jpg"
      toshita_IMAGE = "toshita.jpeg"
      girish_IMAGE = "girish.jpeg"
      adish_IMAGE = "adish.jpg"
      avinash_IMAGE = "avinash.jpeg"
      hardik_IMAGE = "hardik.jpeg"
      html_temp = """
            <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Team</h2>
            </div>
            """
      st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .adish-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .avinash-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .hardik-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .harshal-img {
            float:right;
            width:175px;
            height:192px;
            margin: 0px 0px 0px 28px;
        }
        .tanisha-img {
             float:right;
             margin: 0px 0px 0px 28px;
        }
        .girish-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .kanak-img {
             float:right;
             width:184px;
             height:192px;
             margin: 0px 0px 0px 25px; 
        }
        .toshita-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .vamsi-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        .venkat-img {
             float:right;
             width:175px;
             height:192px;
             margin: 0px 0px 0px 28px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(html_temp,unsafe_allow_html=True)
      st.subheader("Project Manager")
      st.write("• &nbsp;  &nbsp;    [Toshita Sharma](https://www.linkedin.com/in/toshita-sharma-79894a1a4/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="toshita-img" src="data:image/png;base64,{base64.b64encode(open(toshita_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.subheader("Contributors")
      st.write("1. [Tanisha Banik](https://www.linkedin.com/in/tanisha-banik-04b511173/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="tanisha-img" src="data:image/png;base64,{base64.b64encode(open(tanisha_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("2. [Harshal Hirpara](https://www.linkedin.com/in/harshaljhirpara)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="harshal-img" src="data:image/png;base64,{base64.b64encode(open(harshal_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("3. [Venkata Narayana Bommanaboina](https://www.linkedin.com/in/bvnarayana515739)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="venkat-img" src="data:image/png;base64,{base64.b64encode(open(venkat_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("4. [Girish Sahu](https://www.linkedin.com/in/girishsahu)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="girish-img" src="data:image/png;base64,{base64.b64encode(open(girish_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("5. [Shreya Chawla]()")
      st.write("6. [Vamsi Chittor](https://www.linkedin.com/in/vamsi-chittoor-331b80189)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="vamsi-img" src="data:image/png;base64,{base64.b64encode(open(vamsi_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("7. [Hardik Tejani](https://www.linkedin.com/in/hardik-tejani)") 
      st.markdown(
            f"""
            <div class="container">
                  <img class="hardik-img" src="data:image/png;base64,{base64.b64encode(open(hardik_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      ) 
      st.write("8. [Kanak Tekwani](https://www.linkedin.com/in/kanak-tekwani/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="kanak-img" src="data:image/png;base64,{base64.b64encode(open(kanak_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("9. [Adish Golechha](https://www.linkedin.com/in/adish-golechha)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="adish-img" src="data:image/png;base64,{base64.b64encode(open(adish_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("10. [Avinash Das](https://www.linkedin.com/in/avinash-das-794b4b179/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="avinash-img" src="data:image/png;base64,{base64.b64encode(open(avinash_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.write("11. [Larry]()")



