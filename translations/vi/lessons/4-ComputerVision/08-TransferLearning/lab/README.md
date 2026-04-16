# Phân loại thú cưng Oxford bằng Transfer Learning

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Hãy tưởng tượng bạn cần phát triển một ứng dụng cho nhà trẻ thú cưng để phân loại tất cả các thú cưng. Một trong những tính năng tuyệt vời của ứng dụng này là tự động nhận diện giống loài từ một bức ảnh. Trong bài tập này, chúng ta sẽ sử dụng transfer learning để phân loại hình ảnh thú cưng thực tế từ bộ dữ liệu [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Bộ dữ liệu

Chúng ta sẽ sử dụng bộ dữ liệu gốc [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), bao gồm 35 giống chó và mèo khác nhau.

Để tải bộ dữ liệu, sử dụng đoạn mã sau:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Bắt đầu Notebook

Bắt đầu bài thực hành bằng cách mở [OxfordPets.ipynb](OxfordPets.ipynb)

## Kết luận

Transfer learning và các mạng đã được huấn luyện trước giúp chúng ta giải quyết các vấn đề phân loại hình ảnh thực tế một cách tương đối dễ dàng. Tuy nhiên, các mạng đã huấn luyện trước hoạt động tốt với các hình ảnh có tính chất tương tự, và nếu chúng ta bắt đầu phân loại các hình ảnh rất khác biệt (ví dụ: hình ảnh y tế), kết quả có thể sẽ kém hơn đáng kể.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.