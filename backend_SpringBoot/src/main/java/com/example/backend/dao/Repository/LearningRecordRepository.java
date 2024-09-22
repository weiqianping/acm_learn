package com.example.backend.dao.Repository;

import com.example.backend.model.LearningRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LearningRecordRepository extends JpaRepository<LearningRecord, Long> {
    // 自定义查询方法
}
