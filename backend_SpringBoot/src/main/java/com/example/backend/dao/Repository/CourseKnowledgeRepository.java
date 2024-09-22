package com.example.backend.dao.Repository;

import com.example.backend.model.CourseKnowledge;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CourseKnowledgeRepository extends JpaRepository<CourseKnowledge, Long> {
    // 自定义查询方法
}
